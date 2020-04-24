# pkg-example
An example python package as a starter for good research code.

## Installation
Create and activate a virtual environment, then pip install the package. For
example, with conda:

```python
conda create -n pex python=3
conda activate pex
```

Then to install the package, change directory to the root of the package and:
```python
cd /where/the/package/lives/pkg-example
pip install .
# alternatively simply: pip install /where/the/package/lives/pkg-example
```

If you would like to edit the code and for changes to be reflected without the
need to reinstall the package, use pip's `-e` flag:
```python
pip install -e .
```
