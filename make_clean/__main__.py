import argparse

from make_clean.make_clean import Cleaner


def main():
    parser = argparse.ArgumentParser(
        description=u'clean target dir without ignores')
    parser.add_argument(
        'target_dir',
        metavar='TARGET_DIR',
        nargs='+',
        help=u'dir to remove recursively ')
    parser.add_argument(
        '--ignore-file',
        help=u'dir/file file to ignore from remove',
        default='.cleanignore')
    parser.add_argument(
        '-i', '--ignore-patterns',
        help=u'dir/file to ignore from remove',
        nargs='*',
        default=[])

    args = parser.parse_args()
    Cleaner.clean(args.target_dir, args.ignore_file, args.ignore_patterns)


if __name__ == '__main__':
    main()
