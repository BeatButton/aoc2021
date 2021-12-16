from dataclasses import dataclass
from pathlib import Path
from itertools import chain

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()

@dataclass
class Packet:
    version: int
    type_id: int


def to_int(bits):
    return int("".join(map(str, bits)), 2)

def align_up(n):
    return n + 4 - n % 4




bits = list(chain(*(map(int, f"{f'{int(ch, 16):b}':0>4}") for ch in inp)))

def parse(bits):
    idx = 0
    ans = 0
    while idx < len(bits) - 8:
        version = to_int(bits[idx : idx + 3])
        ans += version
        idx += 3
        type_id = to_int(bits[idx : idx + 3])
        idx += 3
        match type_id:
            case 4:
                #n = []
                cont = True
                while cont:
                    #n.extend(bits[idx + 1 : idx + 5])
                    cont = bits[idx] == 1
                    idx += 5
                #n = to_int(n)
            case other:
                length_type = bits[idx]
                idx += 1
                match length_type:
                    case 0:
                        length = to_int(bits[idx:idx+15])
                        idx += 15
                        ans += parse(bits[idx:idx+length])
                        idx += length
                    case 1:
                        idx += 11
                    case other:
                        print(f"invalid length type {other}")
                        exit(1)
    return ans


print(parse(bits))
