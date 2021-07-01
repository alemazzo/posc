import argparse


def get_argument_parser():

    parser = argparse.ArgumentParser(
        description='Setup your OS in one command')

    parser.add_argument('file',
                        help='YAML configuration file')

    return parser


def parse_arguments():
    parser = get_argument_parser()
    args = parser.parse_args()
    return args
