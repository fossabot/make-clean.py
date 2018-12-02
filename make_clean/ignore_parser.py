import os


class IgnoreParser(object):
    def __init__(self, fullpath):
        self.cwd = os.getcwd().replace(os.sep, '/').lstrip('/')
        self.ignores = IgnoreParser._build_ignores(fullpath)

    @classmethod
    def _build_ignores(cls, fullpath):
        ignores = []
        if fullpath and os.path.isfile(fullpath):
            with open(fullpath) as fp:
                ignores.extend([
                    x.strip().replace('/', os.sep) for x in fp
                    if not x.strip().startswith('#')])
        return ignores

    def has_ignored(self, object_fullpath):
        relpath = (str(object_fullpath)
                   .replace(os.sep, '/')
                   .lstrip(self.cwd))
        return False
