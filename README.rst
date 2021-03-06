[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ftomoh1r%2Fmake-clean.py.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Ftomoh1r%2Fmake-clean.py?ref=badge_shield)

==========
make-clean
==========

.. image:: https://github.com/tomoh1r/make-clean.py/workflows/test/badge.svg
   :target: https://github.com/tomoh1r/make-clean.py/actions?query=workflow%3Atest

.. image:: https://ci.appveyor.com/api/projects/status/ui4585dett58eu1r?branch=master&svg=true
   :target: https://ci.appveyor.com/project/jptomo/make-clean-py
   :alt: AppVeyor Build Status

If one'd like to make sphinx repository with github-pages sumodule, one shoud
exclude rm ``_build/html/.git``.

``make-clean`` package provide to keep ``.git`` file with it.

Switch ``make.bat`` file clean to below::

  if "%1" == "clean" (
  	.\path\to\make-clean.exe _build -i _build\html\.git _build\html\.gitignore
  	goto end
  )

Usage
=====

This package has a `make-clean` command.

.. code-block:: bat

   > .\venv\Scripts\make-clean.exe -h
   usage: make-clean-script.py [-h] [--clean-ignore CLEAN_IGNORE]
                               [-i [IGNORE [IGNORE ...]]]
                               TARGET_DIR [TARGET_DIR ...]

   clean target dir without ignores

   positional arguments:
     TARGET_DIR            dir to remove recursively

   optional arguments:
     -h, --help            show this help message and exit
     --clean-ignore CLEAN_IGNORE
                           dir/file file to ignore from remove
     -i [IGNORE [IGNORE ...]], --ignores [IGNORE [IGNORE ...]]
                           dir/file to ignore from remove

Test
====

I use `pytest <http://doc.pytest.org/en/latest/>`__.

.. code-block:: bat

   > C:\path\to\python\3.X.Y\python.exe -m venv --clear venv
   > .\venv\Scripts\python.exe setup.py develop easy_install make-clean[test]
   > .\venv\Scripts\python.exe -m pytest


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ftomoh1r%2Fmake-clean.py.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Ftomoh1r%2Fmake-clean.py?ref=badge_large)