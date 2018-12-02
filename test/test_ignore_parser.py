import pytest


@pytest.mark.parametrize('ignore_text,target_path', [
    # It is file.
    ('piyo.txt', 'hoge/fuga/piyo.txt'),
    # It is directory.
    # Wild card.
    # Wild card (Directory).
])
def test_has_ignored(tmpdir, IgnoreParser, ignore_text, target_path):
    text = tmpdir.join('.cleanignore')
    text.write(ignore_text)

    parser = IgnoreParser(str(text.realpath()))
    assert parser.has_ignored(target_path)


@pytest.mark.parametrize('ignore_text,target_path', [
    # It is file.
    #('foo.txt', 'hoge/fuga/piyo.txt'),
    # It is directory.
    #('foo/', 'hoge/fuga/piyo.txt'),
    # It is force has not ignored (File).
    # It is force has not ignored (Directory).
    # Wild card.
    # Wild card (Directory).
])
def test_has_not_ignored(tmpdir, IgnoreParser, ignore_text, target_path):
    text = tmpdir.join('.cleanignore')
    text.write(ignore_text)

    parser = IgnoreParser(str(text.realpath()))
    assert parser.has_ignored(target_path)
