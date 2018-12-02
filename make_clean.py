# -*- coding: utf-8 -*-
import os
import argparse
import shutil


VERSION = (3, 0, 0)
__version__ = '{0:d}.{1:d}.{2:d}'.format(*VERSION)


def clean(target_dirs, clean_ignore='.cleanignore', ignores=None):
    Clean(target_dirs, clean_ignore, ignores).clean()

    cleaner = Cleaner()
    cleaner.build_ignore(clean_ignore, ignores)
    cleaner.clean(target_dirs)

    '''clean target_dir except ignores relatively

    cleanup target directory except:

    - file: is in ignores
    - directory: is in ignores

    Files and directories are referenced relatively.

    :param str target_dir: target directory to cleanup
    :param list ignores: not rm files or directories
    '''
    target_dirs = [os.path.abspath(x) for x in target_dirs]
    ignore_dirs, ignore_files = parse_ignores(clean_ignore, ignores)
    rm_files(target_dirs, ignore_dirs, ignore_files)
    rm_dirs(target_dirs, ignore_dirs)
    
    parser = IgnoreParser(ignore_fpath, ignores)
    for dir_path in target_dirs:
        for root, _, files in os.walk(dir_path):
            for f in files:
                fpath = os.path.join(root, f)
                if not parser.ignored(fpath):
                    pass

                if (fullpath.startswith(ignore_dirs) or
                        fullpath in ignore_files):
                    continue
                os.remove(fullpath)


class Cleaner(object):
    @classmethod
    def clean(cls, target_dirs, clean_ignore='.cleanignore', ignores=None):
        '''clean target_dir except ignores relatively

        cleanup target directory except:

        - file: is in ignores
        - directory: is in ignores

        Files and directories are referenced relatively.

        :param str target_dir: target directory to cleanup
        :param list ignores: not rm files or directories
        '''
        target_dirs = [os.path.abspath(x) for x in target_dirs]
        ignore_dirs, ignore_files = parse_ignores(clean_ignore, ignores)
        rm_files(target_dirs, ignore_dirs, ignore_files)
        rm_dirs(target_dirs, ignore_dirs)
        
        parser = IgnoreParser(ignore_fpath, ignores)
        for dir_path in target_dirs:
            for root, _, files in os.walk(dir_path):
                for f in files:
                    fpath = os.path.join(root, f)
                    if not parser.ignored(fpath):
                        pass

                    if (fullpath.startswith(ignore_dirs) or
                            fullpath in ignore_files):
                        continue
                    os.remove(fullpath)

    def __init__(self, target_dirs, clean_ignore, ignores):
        self.target_dirs = [os.path.abspath(x) for x in target_dirs]
        ignore_dirs, ignore_files = parse_ignores(clean_ignore, ignores)

    def clean(self):
        self.rm_files(target_dirs, ignore_dirs, ignore_files)
        self.rm_dirs(target_dirs, ignore_dirs)

    def rm_files(self, target_dirs, ignore_dirs, ignore_files):
        """Remove files."""
        for dir_path in target_dirs:
            for root, _, files in os.walk(dir_path):
                for f in files:
                    fullpath = os.path.join(root, f)
                    if (fullpath.startswith(ignore_dirs) or
                            fullpath in ignore_files):
                        continue
                    os.remove(fullpath)

    def rm_dirs(self, target_dirs, ignore_dirs):
        """Remove empty directories."""
        ignore_dir_set = set(ignore_dirs)

        for dir_path in target_dirs:
            for root, _, _ in os.walk(dir_path):
                if (not Cleaner.is_empty_dir(root) or
                        root in ignore_dir_set or
                        root in target_dirs):
                    continue
                shutil.rmtree(root)

    @staticmethod
    def is_empty_dir(target_dir):
        """return is empty directory or not

        :param str target_dir: target dir
        """
        for root, _, files in os.walk(target_dir):
            for f in files:
                if os.path.isfile(os.path.join(root, f)):
                    return False
        return True


class IgnoreParser(object):
    def __init__(self, fpath, patterns):
        self.ignores = IgnoreParser._build_ignores(fpath, patterns)

    @classmethod
    def _build_ignores(cls, fpath, patterns):
        ignores = []
        if ignore_fname and os.path.isfile(ignore_fname):
            with open(ignore_fname) as fp:
                lines = [x.strip() for x in fp if not x.strip().startswith('#')]
            ignores.extend([x.lstrip('/').replace('/', os.sep) for x in lines])

        if ignore_patterns:
            ignores.extend([x.lstrip('/') for x in ignore_patterns if x])
        return ignores

    def ignored(self, fpath):
        fpath = str(fpath)


def parse_ignores(ignore_fname, ignore_patterns):
    ignores = []
    if ignore_fname and os.path.isfile(ignore_fname):
        with open(ignore_fname) as fp:
            lines = [x.strip() for x in fp if not x.strip().startswith('#')]
        ignores.extend([x.lstrip('/').replace('/', os.sep) for x in lines])

    if ignore_patterns:
        ignores.extend([x.lstrip('/') for x in ignore_patterns if x])

    ignore_dirs = tuple(os.path.abspath(x) for x in ignores
                        if x and x.endswith(os.sep) and os.path.isdir(x))
    ignore_files = {os.path.abspath(x) for x in ignores
                    if x and os.path.isfile(x)}
    return ignore_dirs, ignore_files


def rm_files(target_dirs, ignore_dirs, ignore_files):
    """Remove files."""
    for dir_path in target_dirs:
        for root, _, files in os.walk(dir_path):
            for f in files:
                fullpath = os.path.join(root, f)
                if (fullpath.startswith(ignore_dirs) or
                        fullpath in ignore_files):
                    continue
                os.remove(fullpath)


def rm_dirs(target_dirs, ignore_dirs):
    """Remove empty directories."""
    ignore_dir_set = set(ignore_dirs)

    for dir_path in target_dirs:
        for root, _, _ in os.walk(dir_path):
            if (not is_empty_dir(root) or
                    root in ignore_dir_set or
                    root in target_dirs):
                continue
            shutil.rmtree(root)


def is_empty_dir(target_dir):
    """return is empty directory or not

    :param str target_dir: target dir
    """
    for root, _, files in os.walk(target_dir):
        for f in files:
            if os.path.isfile(os.path.join(root, f)):
                return False
    return True


def main():
    parser = argparse.ArgumentParser(
        description=u'clean target dir without ignores')
    parser.add_argument(
        'target_dir',
        metavar='TARGET_DIR',
        nargs='+',
        help=u'dir to remove recursively ')
    parser.add_argument(
        '--clean-ignore',
        metavar='CLEAN_IGNORE',
        help=u'dir/file file to ignore from remove',
        default='.cleanignore')
    parser.add_argument(
        '-i', '--ignores',
        metavar='IGNORE',
        help=u'dir/file to ignore from remove',
        nargs='*',
        default=[])

    args = parser.parse_args()
    Cleaner.clean(args.target_dir, args.clean_ignore, args.ignores)


if __name__ == '__main__':
    main()
