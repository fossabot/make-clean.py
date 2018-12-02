import os

import pytest


@pytest.mark.parametrize(
        'ignores,is_exists', [
            # test for remove file
            ([], False),
            # test for do not remove excluded file
            (['example.txt'], True)
        ])
def test_remove_file(monkeypatch, clean, tmp_dir,
                     ignores, is_exists):
    dir_name = os.path.basename(tmp_dir)
    monkeypatch.chdir(os.path.dirname(tmp_dir))

    target_file = os.path.join(tmp_dir, 'example.txt')
    open(target_file, 'w').close()

    ignores = [os.path.join(dir_name, x) for x in ignores]

    assert os.path.exists(target_file)
    clean([dir_name], ignore_patterns=ignores)
    assert os.path.exists(target_file) == is_exists


@pytest.mark.parametrize(
        'files,ignores,is_exists', [
            # test for remove dir
            ([], [], False),
            # test for do not remove not empty dir
            (['example.txt'], [os.path.join('example', 'example.txt')], True),
            # test for do not remove excluded dir
            ([], ['example' + os.sep], True)
        ])
def test_remove_dir(monkeypatch, clean, tmp_dir,
                    files, ignores, is_exists):
    dir_name = os.path.basename(tmp_dir)
    monkeypatch.chdir(os.path.dirname(tmp_dir))

    target_dir = os.path.join(tmp_dir, 'example')
    os.mkdir(target_dir)

    for fname in files:
        target_file = os.path.join(target_dir, fname)
        open(target_file, 'w').close()

    ignores = [os.path.join(dir_name, x) for x in ignores]

    assert os.path.exists(target_dir)
    clean([dir_name], ignore_patterns=ignores)
    assert os.path.exists(target_dir) == is_exists


def test_donot_remove_dir_without_ossep_suffix(
        monkeypatch, clean, tmp_dir):
    dir_name = os.path.basename(tmp_dir)
    monkeypatch.chdir(os.path.dirname(tmp_dir))

    target_dir = os.path.join(tmp_dir, 'example')
    os.mkdir(target_dir)

    assert os.path.exists(target_dir)
    clean([dir_name],
               ignores=[os.path.join(dir_name, 'example')])
    assert not os.path.exists(target_dir)


@pytest.mark.parametrize(
        'prefix', [
            # test for remove file
            (''),
            # test for starts with slash
            ('/')
        ])
def test_not_remove_exclude_file_from_file(monkeypatch, clean, tmp_dir,
                                           prefix):
    dir_name = os.path.basename(tmp_dir)
    monkeypatch.chdir(os.path.dirname(tmp_dir))

    target_dir = os.path.join(tmp_dir, 'example')
    os.mkdir(target_dir)
    target_file = os.path.join(target_dir, 'example.txt')
    open(target_file, 'w').close()

    with open('.cleanignore', 'w') as fp:
        fp.write(prefix + dir_name + '/example/example.txt')

    assert os.path.exists(target_file)
    clean([dir_name], '.cleanignore')
    assert os.path.exists(target_file)


def test_clean_current_dir(monkeypatch, clean, tmp_dir):
    monkeypatch.chdir(tmp_dir)

    target_file = os.path.join(tmp_dir, 'example.txt')
    open(target_file, 'w').close()

    assert os.path.exists(tmp_dir)
    assert os.path.exists(target_file)
    clean('.')
    assert os.path.exists(tmp_dir)
    assert not os.path.exists(target_file)


def test_clean_dirs(monkeypatch, clean, tmp_dir):
    dir_name = os.path.basename(tmp_dir)
    monkeypatch.chdir(os.path.dirname(tmp_dir))
    here = os.getcwd()

    dir_names = [os.path.join(dir_name, x) for x in ['exmaple0', 'example1']]
    for dname in dir_names:
        os.mkdir(dname)
        target_file = os.path.join(here, dname, 'example.txt')
        open(target_file, 'w').close()

    for dname in dir_names:
        assert os.path.exists(os.path.join(here, dname, 'example.txt'))
    clean(dir_names)
    for dname in dir_names:
        assert not os.path.exists(os.path.join(here, dname, 'example.txt'))
