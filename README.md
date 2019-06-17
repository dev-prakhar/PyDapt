[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/dev-prakhar/flexible-object/branch/master/graph/badge.svg)](https://codecov.io/gh/dev-prakhar/flexible-object)
[![Build Status](https://travis-ci.com/dev-prakhar/flexible-object.svg?branch=master)](https://travis-ci.com/dev-prakhar/flexible-object)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

# Flexible Object

Flexible objects coverts a dictionary into an object.
It is similar to the [OpenStruct](https://ruby-doc.org/stdlib-2.5.1/libdoc/ostruct/rdoc/OpenStruct.html) of ruby.

# Installation

```
Python Verions Required >= 3
```
```
pip install flexible-object
```

# Usage

### Converting a dictionary to Object

```python
from flexible_object.models import FlexibleObject

dictionary = {"test": 1, "test1": {"test2": 2}}
flexible_object = FlexibleObject(dictionary)

print(flexible_object.test) # 1
print(flexible_object.test1.test2) # 2
```

### Converting a dictionary to Object with kwargs

```python
from flexible_object.models import FlexibleObject

dictionary = {"test": 1, "test1": {"test2": 2}}
flexible_object = FlexibleObject(dictionary, test3=3, test4=4)

print(flexible_object.test) # 1
print(flexible_object.test1.test2) # 2
print(flexible_object.test3) # 3
print(flexible_object.test4) # 4
```

### Deleting an attribute

```python
from flexible_object.models import FlexibleObject

dictionary = {"test": 1, "test1": {"test2": 2}}
flexible_object = FlexibleObject(dictionary)

print(flexible_object.test) # 1
print(flexible_object.test1.test2) # 2

flexible_object.drop('test3') # None
flexible_object.drop('test1') # 1

print(flexible_object.test1) # AttributeError: 'FlexibleObject' object has no attribute 'test1'
```
