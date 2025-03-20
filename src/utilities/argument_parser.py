from typing import List, Optional, Any
import argparse


class ArgumentParser:
    def __init__(self, prog: str = "parser") -> None:
        self._parser = argparse.ArgumentParser(
            prog=prog,
            add_help=True,
        )

        self._subparsers = self._parser.add_subparsers(dest="subcommand")

    def register_subcommand(
        self,
        subcommand: str,
        arguments: List[str],
        helps: List[str],
        defaults: Optional[List[Optional[Any]]] = None,
        required: Optional[List[bool]] = None,
    ) -> "ArgumentParser":
        if len(arguments) != len(helps):
            raise ValueError("Arguments and helps must have the same length.")

        if defaults is not None and len(arguments) != len(defaults):
            raise ValueError("Arguments and defaults must have the same length.")

        if required is not None and len(arguments) != len(required):
            raise ValueError("Arguments and required flags must have the same length.")

        if defaults is None:
            defaults = [None] * len(arguments)
        if required is None:
            required = [False] * len(arguments)

        command_parser = self._subparsers.add_parser(subcommand)

        for argument, help_text, default, is_required in zip(
            arguments, helps, defaults, required
        ):
            command_parser.add_argument(
                argument, help=help_text, default=default, required=is_required
            )

        return self

    def parse_arguments(
        self, arguments: Optional[List[str]] = None
    ) -> argparse.Namespace:
        if arguments is None:
            arguments = ["--help"]

        return self._parser.parse_args(arguments)
