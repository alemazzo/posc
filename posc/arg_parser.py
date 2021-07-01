import argparse


def getParser():

    parser = argparse.ArgumentParser(
        description='Setup your OS in one command')

    parser.add_argument('--config', required=True,
                        help='YAML configuration file')

    return parser
