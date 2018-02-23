from setuptools import setup, find_packages
setup(
    name="helloworld",
    version="0.1",
    packages=find_packages(), 
    author="Chloe Hacker",
    license="GPLv3",
    description="A package for giving your dog a treat"
    classifiers=["Programming Language :: Python :: 3"]
    entry_points={
        'console_scripts': ['helloworld = helloworld.__main__:main']
        }
)