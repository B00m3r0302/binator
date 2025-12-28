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
        self.parser.add_argument(
            "target",
            help="Path to binary or directory to analyze",
        )

        self.parser.add_argument(
            "--mode",
            choices=["static", "strings", "headers"],
            default = "static",
            help="Analysis mode to run",
        )

        self.parser.add_argument(
            "--verbose",
            action="store_true",
            help="Enable verbose output",
        )

    def run(self, argv: list[str] | None = None) -> int:
        args = self.parser.parse_args(argv)
        
        if args.verbose:
            self._log_verbose(args)

        match args.mode:
            case "static":
                self.run_static_analysis(args.target)
            case "strings":
                self.run_strings(args.target)
            case "headers":
                self.run_headers(args.target)
            case default:
                self.run_static_analysis(args.target)

    def _log_verbose(self, args: argparse.Namespace) -> None:
        print("[*] Running in verbose mode")
        printf(f"[*] Target {argv.target}")
        printf(f"[*] Mode: {args.mode}")

    def run_static_analysis(self, target: str) -> None:
        printf(f"[+] Running static analysis on {target}")

    def run_strings(self, target: str) -> None:
        printf(f"[+] Extracting strings from {target}")

    def run_headers(self, target: str) -> None:
        printf(f"[+] Parsing headers from {target}")

def main() -> int:
    cli = BinatorCLI()
    return cli.run()

if __name__ == "__main__":
    sys.exit(main())
