# -*- coding: utf-8 -*-
from __future__ import absolute_import

import importlib
import os
import shutil
import tempfile

import pytest


@pytest.fixture(scope='module')
def make_clean():
    cls = importlib.import_module('make_clean.make_clean').Cleaner
    return cls.clean


@pytest.fixture(scope='function')
def tmp_dir(monkeypatch):
    '''manage create and delete temporary directory

    I need real directory, so I can't use tmpdir...
    (or directory basename)
    '''
    try:
        tmp_dir = tempfile.mkdtemp()
        yield tmp_dir
    finally:
        # tmp_dir を削除するためにカレントディレクトリを移動
        monkeypatch.chdir(os.path.dirname(tmp_dir))
        shutil.rmtree(tmp_dir)
