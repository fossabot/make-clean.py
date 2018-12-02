import os


class IgnoreParser(object):
    def __init__(self, fpath, patterns):
        self.ignores = IgnoreParser._build_ignores(fpath, patterns)

    @classmethod
    def _build_ignores(cls, fpath, patterns):
        ignores = []
        if fpath and os.path.isfile(fpath):
            with open(fpath) as fp:
                ignores.extend([
                    x.strip().replace('/', os.sep) for x in fp
                    if not x.strip().startswith('#')])

        if patterns:
            ignores.extend([x.lstrip('/') for x in patterns if x])
        return ignores

    def has_ignored(self, object_path):
        fpath = str(object_path)
        return False
