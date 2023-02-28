from setuptools import setup, find_packages

version = '0.1.0'
description = 'A To-Do List application featuring natural language support.'

# Link the description to be the same README as in the Github repo
with open('README.md') as f:
    long_description = f.read()

# Setting up
setup(
    name="ndy-cli",
    version=version,
    author="neomoon007 (Marcos Costa)",
    url='https://github.com/neomoon007/ndy-cli',
    description=description,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['termcolor'],
    keywords=['python', 'cli', 'todolist'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
