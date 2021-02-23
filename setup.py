import setuptools

with open("README.md", "r") as fh: 
    
    long_description = fh.read()
    
setuptools.setup(

        name="sai2048",

        version="1.0.0",

        author="Sai Krishna Karnati",

        author_email="saikrishna.carnati@gmail.com", 
        
        long_description_content_type="text/markdown",

        description="A small 2048 game library",

        long_description=long_description,

        url="https://github.com/saikrishna7004/sai2048",

        packages=setuptools.find_packages (),

        classifiers=[ 
        
        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License", 
        
        "Operating System :: OS Independent",
        
        ],

        python_requires='>=3.6',
    
)