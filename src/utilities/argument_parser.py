from typing import List, Optional
import argparse


class ArgumentParser:
    def __init__(self, prog: str = "parser") -> None:
        self._parser = argparse.ArgumentParser(
            prog=prog,
            add_help=True,
        )

        self._subparsers = self._parser.add_subparsers(dest="subcommand")

    def register_subcommands(
        self, subcommand: str, arguments: List[str], helps: List[str]
    ) -> None:
        if len(arguments) != len(helps):
            raise ValueError("Arguments and helps must have the same length.")

        command_parser = self._subparsers.add_parser(subcommand)

        for argument, help_text in zip(arguments, helps):
            command_parser.add_argument(argument, help=help_text)

    def parse_arguments(
        self, arguments: Optional[List[str]] = None
    ) -> argparse.Namespace:
        if arguments is None:
            arguments = ["--help"]

        return self._parser.parse_args(arguments)
