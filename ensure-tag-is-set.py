from typing import Sequence
import argparse

PASS = 0
FAIL = 1


def main(argv: Sequence[str] | None = None) -> int:
    print("HELLO WORLD")
    """ parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    retv = PASS

    return retv """


if __name__ == "__main__":
    raise SystemExit(main())
