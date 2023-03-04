# dly-algs
A collection of python algorithms to complete trivial tasks.

## Algorithms

### deep_merge
Deep merges two dictionaries and returns a merged copy. Supports and respects nested dictionaries.

#### Usage:
```python
from dly_algs import deep_merge

x_dict = {"a": 1, "b": {"c": 1, "d": 1}}
y_dict = {"b": {"c": 2, "e": 2}}
deep_merge(x_dict, y_dict)
# {"a": 1, "b": {"c": 2, "d": 1, "e": 2}}
```
### deep_compare
Deep compares two dictionaries. Supports usage with nested dictionaries.

#### Usage
```python
from dly_algs import deep_compare

x_dict = {"a": {"b": 1, "c": 1}}
y_dict = {"a": {"b": 1, "c": 1}}
z_dict = {"a": {"b": 1, "c": 2}}

deep_compare(x_dict, y_dict)
# True

deep_compare(y_dict, z_dict)
# False
```