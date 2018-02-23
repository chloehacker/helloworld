import argparse
import helloworld


def parse_command_line():
    " parses args for the helloworld.py funtions"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add short args
    parser.add_argument(
        "-n", "--name",
        help="optional name to say hello to",
        type=str)

    # add long args
    parser.add_argument(
        "--howlong",
        help="print days until Darwin's next birthday",
        action="store_true")

    parser.add_argument(
        "--countdown",
        help="print predicted days until end of the world",
        action="store_true")

    # parse args
    args = parser.parse_args()
    return args


def main():
    " run helloworld on parsed args"
    args = parse_command_line()
    helloworld.helloworld(
        name=args.name,
        howlong=args.howlong,
        countdown=args.countdown)