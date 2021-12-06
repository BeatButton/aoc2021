# written by danny and edited by me thanks danny

import pathlib
import argparse
import requests


def get_session() -> str:
    with open(".session", "r") as fp:
        return fp.read()


def download(day: int) -> bytes:
    cookies = {"session": get_session()}
    url = f"https://adventofcode.com/2021/day/{day}/input"
    resp = requests.get(url, cookies=cookies)
    resp.raise_for_status()
    return resp.content


source_template = """from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


"""


def make_day(day: int, input: bytes):
    path = pathlib.Path(f"day_{day:02}/")
    path.mkdir(parents=True, exist_ok=True)
    with open(path / "input", "wb") as fp:
        fp.write(input)

    with open(path / "test", "w"):
        pass

    with open(path / "main.py", "w") as fp:
        fp.write(source_template)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, help="The day of the AoC puzzle")
    args = parser.parse_args()
    input = download(args.day)
    make_day(args.day, input)


if __name__ == "__main__":
    main()
