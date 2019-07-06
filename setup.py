import io

import setuptools


def readme():
    with io.open('README.md', 'r', encoding='utf8') as f:
        return f.read()


setuptools.setup(
    name='pydapt',
    version='0.1',
    author="Prakhar Shrivastava",
    author_email="prakhars1996@gmail.com",
    description="Ruby's OpenStruct for python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/dev-prakhar/pydapt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
