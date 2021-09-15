#coding=UTF-8
from itertools import combinations
from loguru import logger
from abc import ABC, abstractmethod
import wget
import os,pkg_resources
import zipfile

_init_location = pkg_resources.resource_filename(__name__,'__init__.py')
_module_dir_path = os.path.dirname(_init_location)

class TagReconstruct(ABC):
    def __init__(self,align_dict_path):
        self._dict_file_path = os.path.join(_module_dir_path,'list')
        if not os.path.isdir(self._dict_file_path):
            logger.warning("Start download data, ** do not interrupt. **")
            os.makedirs(self._dict_file_path,exist_ok=True)
            self._download_file('https://github.com/NLU-Law-Tech/TagReconstruct/releases/download/list-v1.1/list.zip','list.zip')
            with zipfile.ZipFile(os.path.join(_module_dir_path,'list/list.zip'), 'r') as zip_ref:
                zip_ref.extractall(os.path.join(_module_dir_path,'list'))
        if os.path.exists(align_dict_path):
            pass
        else:
            align_dict_path = os.path.join(_module_dir_path,'list',align_dict_path)
        
        # load dict
        with open(align_dict_path,'r',encoding='utf-8') as f:
            _list = f.read().strip().split()
        
        # create dict
        self.align_dict = {}
        for key in _list:
            self.align_dict[key] = None
        
        logger.info("Create align_dict successful. Size: %d"%len(self.align_dict))

    def _download_file(self,url,f_name):
        wget.download(url,os.path.join(self._dict_file_path,f_name))
    
    def list_combination_results(self,context,min_len=1,max_len=None):
        """
        對context做組合，列出所有可能
        """
        if max_len is None:
            max_len = len(context)
        combination_results = []
        for i in range(min_len,max_len+1):
            combination_len = i  
            for result in combinations(context,combination_len):
                # print(result,end='\r')
                result = ''.join(result)
                if result in self.align_dict:
                    combination_results.append(result)
        # Sort by length (longest first)
        combination_results = sorted(combination_results,key=lambda x:-1*len(x))
        return combination_results
    
    def filter_tag_is_subset_of_results(self,tag,results):
        outs = []
        for result in results:
            is_char_all_appear_in_result = True
            for t in tag:
                if t not in result:
                    is_char_all_appear_in_result = False
            if is_char_all_appear_in_result:
                outs.append(result)
        return outs

    @abstractmethod    
    def run(self):
        pass

class SearchInContext(TagReconstruct):
    """
    嘗試在內文中尋找
    """         
    def run(self,context,tag,bound=5,max_look_ahead=20,max_look_back=20):
        min_len = len(tag)-bound
        if min_len <=5: min_len=5;
        max_len = len(tag)+bound
        # 先找到tag第一次出現的地方
        tag_start_at = context.index(tag)
        outs = []
        
        # 往前找找
        _new_context_start_at = tag_start_at-max_look_ahead
        if _new_context_start_at <0: _new_context_start_at = 0;
        _context = context[_new_context_start_at:tag_start_at]
        combination_results = self.list_combination_results(_context,min_len=min_len,max_len=max_len)
        outs += self.filter_tag_is_subset_of_results(tag,combination_results)
        
        # 往後找找
        _new_context_end_at = tag_start_at+max_look_back
        _context = context[tag_start_at:_new_context_end_at]
        combination_results = self.list_combination_results(_context,min_len=min_len,max_len=max_len)
        outs += self.filter_tag_is_subset_of_results(tag,combination_results)

        # 依照長度排序
        outs = sorted(outs,key=lambda x:-1*len(x))
        
        if len(outs) == 0:
            return tag
        return outs[0]


class SearchNearby(TagReconstruct):
    """
    嘗試在tag周圍尋找
    """
    def run(self,context,start_at,end_at,bound,tag=None):
        assert start_at <= end_at,'start_at must smaller than end_at'
        if tag is None:
            tag = context[start_at:end_at]
        # 將tag範圍擴大
        new_context = context[start_at-bound:end_at+bound]
        combination_results = self.list_combination_results(new_context,min_len=len(tag),max_len=len(tag)+8)
        combination_results = self.filter_tag_is_subset_of_results(tag,combination_results)
        
        if len(combination_results) == 0:
            return tag
        return combination_results[0]
