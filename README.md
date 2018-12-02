# make-clean

[![Travis CI Build Status](https://travis-ci.org/tomoh1r/make-clean.py.svg?branch=master)](https://travis-ci.org/tomoh1r/make-clean.py) [![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/ui4585dett58eu1r?branch=master&svg=true)](https://ci.appveyor.com/project/tomoh1r/make-clean-py)

If one'd like to make sphinx repository with github-pages sumodule, one shoud
exclude rm `_build/html/.git`.

`make-clean` package provide to keep `.git` file with it.

Switch `make.bat` file clean to below

```
if "%1" == "clean" (
	.\path\to\make-clean.exe _build -i _build\html\.git _build\html\.gitignore
	goto end
)
```

## Usage

This package has a `make-clean` command.

```
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
```

## Development

```
> C:\path\to\python\3.X.Y\python.exe -m venv --clear venv
> .\venv\Scripts\python.exe -m pip install -e '.[test,pypi]'
```

## Unit Test

I use [pytest](http://doc.pytest.org/en/latest/).

```
> .\venv\Scripts\python.exe -m pytest
```
