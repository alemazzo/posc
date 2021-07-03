import argparse


def get_argument_parser():

    parser = argparse.ArgumentParser(
        description='Setup your OS in one command')

    parser.add_argument('file',
                        help='YAML configuration file')

    parser.add_argument('--tasks',  action="store_true",
                        help='Print available tasks')

    parser.add_argument('-t',
                        help='Task to execute ([all] for executing all tasks)')

    return parser


def parse_arguments():
    parser = get_argument_parser()
    args = parser.parse_args()
    return args
