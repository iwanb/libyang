## Requirements

* cmake >= 3.1
* swig
* python2 or 3
* setuptools

## Install

```
$ cmake -DPYTHON_BINDING=ON ..
$ make
$ cd python
$ python setup.py install
```

More details on swig's python bindings can be found at [SWIG](http://www.swig.org/Doc3.0/Python.html).

## Usage

Import the libyang package with.

```
import libyang
```
