# -*- coding: utf-8 -*-
import os
import shutil

from make_clean.ignore_parser import IgnoreParser


class Cleaner(object):
    @classmethod
    def clean(cls, target_dirs, ignore_fpath='.cleanignore',
              ignore_patterns=None):
        cleaner = cls()
        cleaner.setup_ignore(ignore_fpath, ignore_patterns)
        cleaner.clean_targets(target_dirs)

    def setup_ignore(self, ignore_fpath, ignore_patterns):
        self._ignore_parser = None
        if ignore_fpath or ignore_patterns:
            self._ignore_parser = IgnoreParser(ignore_fpath, ignore_patterns)

    def has_ignored(self, object_path):
        if self._ignore_parser:
            return self._ignore_parser.has_ignored(object_path)
        return False

    def clean_targets(self, target_dirs):
        """clean target_dir except ignores relatively

        cleanup target directory except:

        - file: is in ignores
        - directory: is in ignores

        Files and directories are referenced relatively.

        :param str target_dir: target directory to cleanup
        :param list ignores: not rm files or directories
        """
        for dir_path in [os.path.abspath(x) for x in target_dirs]:
            for root, _, files in os.walk(dir_path):
                for f in files:
                    fpath = os.path.join(root, f)
                    if not self.has_ignored(fpath):
                        os.remove(fpath)

            for root, _, files in os.walk(dir_path):
                if not self.has_ignored(root):
                    self.rm_dirs(target_dirs)

    def rm_dirs(self, target_dirs):
        """Remove empty directories."""
        for dir_path in target_dirs:
            for root, _, _ in os.walk(dir_path):
                if (not Cleaner.is_empty_dir(root) or
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
