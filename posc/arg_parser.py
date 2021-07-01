import argparse


def getParser():

    parser = argparse.ArgumentParser(
        description='Setup your OS in one command')

    parser.add_argument('config',
                        help='YAML configuration file')

    return parser