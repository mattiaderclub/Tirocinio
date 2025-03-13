import sys
import logging

import pandas as pd

from utilities.logging_config import setup_logging
from utilities.argument_parser import ArgumentParser

setup_logging()
logger = logging.getLogger(__name__)


def prepare_data(input_path: str, output_path: str):
    logger.info("Preparing data...")

    df = pd.read_csv(input_path)
    print(df.info())


if __name__ == "__main__":
    parser = ArgumentParser("fl-ids")

    parser.register_subcommands(
        "prepare",
        ["--input", "--output"],
        ["The input path for the data.", "The output path for the prepared data."],
    )
    args = parser.parse_arguments(sys.argv[1:])

    if args.subcommand == "prepare":
        prepare_data(args.input, args.output)
