# pkg-example
An example python package as a starter for good research code.


## Installation
Create and activate a virtual environment (venv), then pip install the package.
For example, with conda:

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

### Developer mode

If you would like to edit the code and for changes to be reflected without the
need to reinstall the package, use pip's `-e` flag:
```python
pip install -e .
```

--------

:point_up: You'd write install instructions like the above in the `README.md` of
every package you create. If your package required system installations (e.g.
a c++ library), you'd list instructions for that install here too. For an
example, see the install instructions for a package like
[soundfile](https://pysoundfile.readthedocs.io/en/latest/#installation).

--------


## So...what's happened?!

### The python package
Your package, i.e. the code in `./src/pkg_example`, is available for use! Try
it!
```bash
# Check you're using the python of your venv
which python
# Spin it up!
python
>>> import pkg_example
>>> # Handy tip - where is this installed package on your system?!
>>> pkg_example.__file__
```

How? You listed it as a package to install in `setup.cfg`. Relevant lines:
```
packages = find:
package_dir =
    =src
```
Any folder inside `./src` with an `__init__.py` inside will have been picked up
as a package to install.

Importantly, this means you don't need to mess around with relative imports
**within** your package (e.g. `from .calculator_module import Calculator`), just
reference it like a normal package e.g.
`from pkg_example.calculator_module import Calculator`.

> A gotcha to note - you cant have a `-` in your package name for python, only
underscores. The minus sign is a reserved character. I used a minus sign for the
top level folder name to make it clear that this folder is *not* the python
package; the folder `./src/pkg_example` is the folder containing the python
package code.

### Scripts
The script `./scripts/calc` is also available on your path:
```bash
# calc is in the bin of your venv
which calc
# note that the venv bin folder is on your path
echo $PATH
```
It will be in the `bin` folder of your venv, which will have been added
to your [`$PATH`](http://www.linfo.org/path_env_var.html), so, wherever you are
located on your system, if the venv is activated, you can just type calc to
use your package. Neat.

How? Again, you listed this script as something to install in `setup.cfg`.
Relevant lines:
```
scripts =
    scripts/calc
```

### The virtual environment
In addition, your venv has all the packages installed that your package
requires. Relevant lines in `setup.cfg`:

```
install_requires =
    black
    fire
    ipython
    pylint
    pytest
...
[options.extras_require]
dev =
    twine
```

That `options.extras_require` is fancy: as a developer, you'll likely want to
install packages which wont be necessary for the general user. This is an
optional flag you can use on the pip install, e.g.
```bash
pip install -e /where/the/package/lives/pkg-example[dev]
```
will install the package in development mode (`-e`), install all the
`install_requires` packages, *and* the `dev` option package(s), just `twine`
here.


## What next?
You can upload your package to PyPI! See [docs/pypi-publish.md](docs/pypi-publish.md)
for more information. Once you do that, everyone in the world can mash

```bash
pip install your_package_name
```

into their console, and just crack on. Neat huh?!

## Linting & Testing
You will have installed `pytest`, `black`, and `pylint` as part of the installation.

* Running `pytest` from the root directory will run all the tests in `./test`.
* Running `black .` will reformat your code to fit with a specific standard (e.g.
  line lengths etc.)
* Running `pylint pkg_example` will check the package conforms to pep8 standards.

Motivation for testing and linting:

* Python is permissive and not precompiled
* If your code doesn't need to 'go there' it wont
* ...so it wont error till you're 28 hours into the job
* you know, the very important job due for yesterday?

So imagine the scenario:
* You renamed a variable
* Your code is much more understandable, great job!
* ...oops you missed one (your `ctrl` + `f` regex didn't account for bracket first)
* What would have saved your ass:
    * having written a test that runs that part of the code
    * simply running pylint - `unused-variable (W0612)`
    * YOU LITERALLY JUST SAVED 24-26 HOURS (You spent 2-4 writing better code - 
      this gets significantly faster with practice)

## References

* [The (crappy) slides from the talk][1]
* [A great blog post on pacakging your python project][2]
* [The Python Fire Project - super easy CLIs][3]
* [Comments & docstrings a la the **Google Style Guide**][4]
* [...but combine the above with **type hinting** and you're golden][5]
* [More on setup.cfg][6]


[1]: https://docs.google.com/presentation/d/1dZXcjCLKMEpq_HbjI0L4A_ZVMjBmEVN3mbOytily-78/edit?usp=sharing "Slides from the talk"
[2]: https://realpython.com/pypi-publish-python-package/ "Packaging your python project"
[3]: https://github.com/google/python-fire "python fire"
[4]: http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings "Google code styleguide - conmments and docstrings"
[5]: https://docs.python.org/3/library/typing.html "Type hints"
[6]: https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files "setup.cfg"
