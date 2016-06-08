===============
CFD with Python
===============

    :Author: Sriram Krishnaswamy



Description
-----------

This is a personal repository for learning the best practices in terms of Python and project management. I chose to do it in CFD because that's what I know.

For now, the aim of this repository is to provide well documented and tested code for some basic CFD purposes. I use `my codes from a graduate level CFD course <https://github.com/sriramkswamy/CFDEGM6342>`_ and `Lorena Barba's course on CFD <http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/>`_. In the future, I plan to include/fork some of the `other works from her lab <http://lorenabarba.com/code/>`_. The secondary goal is to follow some best practices when it comes to Git and GitHub such as proper branching, tagging releases, etc. Finally, I also intend to create a GitHub pages branch that uses Org mode to create literate programming examples.

If you are looking for high level fluid simulation/solving libraries, you can try `PyFOAM <https://openfoamwiki.net/index.php/Contrib/PyFoam#Short_description>`_ or `fluiddyn <https://pypi.python.org/pypi/fluiddyn/0.0.12a4>`_. If you are looking for CFD General Notation System helper, you can try `pyCGNS <https://pypi.python.org/pypi/pyCGNS>`_.

The project structure and many conventions are taken from `Hitchiker's guide to Python <http://docs.python-guide.org/en/latest>`_.

Requirements
------------

This project requires `sphinx <http://www.sphinx-doc.org/en/stable/>`_ for documentation, `pytest <http://pytest.org/latest/>`_ for testing, `numpy <http://www.numpy.org>`_ for scientific computing and `matplotlib <http://matplotlib.org>`_ for plotting. It is also suggested to use `ipython <https://ipython.org>`_ for a better REPL or if you need to access Dr. Barba's `ipython notebooks <https://github.com/barbagroup/CFDPython>`_ (now called jupyter notebooks).

The requirements are already present in a `text file <./requirements.txt>`_ in this repository. To install using that, just run the following command from the root of this project with your favorite shell `after installing pip <https://pip.pypa.io/en/stable/installing/>`_ for your version of Python.

.. code-block:: sh

    pip install -r requirements.txt

You can install this in a `virtual environment <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_ if you don't want the packages to interfere with your default system ones. Note that this does NOT install ``ipython``. You need to install that separately if you need it.

Usage
-----

A `Makefile <./Makefile>`_ is provided along with this repository. To setup the project, use the following command.

.. code-block:: sh

    make init

To run the tests, use the following command.

.. code-block:: sh

    make tests

Goals
-----

- ☑ Establish some goals in the README

- ☑ Create the project structure

- ☐ Start with UF CFD coursework

- ☐ Add tests using `py.test <http://pytest.org/latest/>`_

- ☐ Add documentation using `sphinx <http://www.sphinx-doc.org/en/stable/>`_

- ☐ Release it as a library/module

- ☐ Establish a ``gh-pages`` branch and add Org file explanations

- ☐ Create a usage section in the README

- ☐ Start developing Lorena Barba's course in a new feature branch

- ☐ Add lesson by lesson

- ☐ Document each lesson's module and test the code (if applicable)

- ☐ Add notes to the ``gh-pages`` page to build on top of the course videos and notes

- ☐ Check out the other works to see if something is interesting

- ☐ Maybe add this to the PyPI?

License
-------

MIT. For a full license statement, `check the license file <./LICENSE>`_.
