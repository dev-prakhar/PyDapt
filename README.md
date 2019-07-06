[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/dev-prakhar/pydapt/branch/master/graph/badge.svg)](https://codecov.io/gh/dev-prakhar/pydapt)
[![Build Status](https://travis-ci.com/dev-prakhar/pydapt.svg?branch=master)](https://travis-ci.com/dev-prakhar/pydapt)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

# Flexible Object

Flexible objects coverts a dictionary into an object.
It is similar to the [OpenStruct](https://ruby-doc.org/stdlib-2.5.1/libdoc/ostruct/rdoc/OpenStruct.html) of ruby.

# Installation

```
Python Version Required >= 3
```
```
pip install pydapt
```

# Usage

### Converting a dictionary to Object

```python
from pydapt.models import PyFlex

dictionary = {"test": 1, "test1": {"test2": 2}}
pyflex = PyFlex(dictionary)

print(pyflex.test) # 1
print(pyflex.test1.test2) # 2
```

### Converting a dictionary to Object with kwargs

```python
from pyflex.models import PyFlex

dictionary = {"test": 1, "test1": {"test2": 2}}
pyflex = PyFlex(dictionary, test3=3, test4=4)

print(pyflex.test) # 1
print(pyflex.test1.test2) # 2
print(pyflex.test3) # 3
print(pyflex.test4) # 4
```

### Deleting an attribute

```python
from pyflex.models import PyFlex

dictionary = {"test": 1, "test1": {"test2": 2}}
pyflex = PyFlex(dictionary)

print(pyflex.test) # 1
print(pyflex.test1.test2) # 2

pyflex.drop('test3') # None
pyflex.drop('test') # 1

print(pyflex.test) # AttributeError: 'PyFlex' object has no attribute 'test'
```
