import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="TagReconstruct", 
    version='0.0.1',
    description="TagReconstruct", #簡介
    long_description=long_description, #顯示於 pypi 的介紹
    long_description_content_type="text/markdown",
    url="https://github.com/NLU-Law-Tech/TagReconstruct",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires = [
        'loguru',
        'wget'
    ]
)