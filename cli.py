import argparse
import sys

class BinatorCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="binator",
            description="Binary reconnaissance and analysis toolkit",
        )
        self._register_arguments()

    def _register_arguments(self) -> None:
