from pathlib import Path
from itertools import chain
from math import prod

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()



def to_int(bits):
    return int("".join(map(str, bits)), 2)

bits = list(chain(*(map(int, f"{f'{int(ch, 16):b}':0>4}") for ch in inp)))


idx = 0
ans = 0
subpacket_info = []
args_stack = []
op_stack = []

while True:
    strt = idx
    new_info = None
    while subpacket_info and subpacket_info[-1][0] <= 0:
        _, num_args, _ = subpacket_info.pop()
        args = []
        for _ in range(num_args):
            args.append(args_stack.pop())
        args.reverse()
        match op_stack.pop():
            case 0:
                res = sum(args)
            case 1:
                res = prod(args)
            case 2:
                res = min(args)
            case 3:
                res = max(args)
            case 5:
                res = args[0] > args[1]
            case 6:
                res = args[0] < args[1]
            case 7:
                res = args[0] == args[1]
            case other:
                print(f"invalid op {other}")
                exit(1)
        args_stack.append(res)

    if idx > len(bits) - 8:
        break

    version = to_int(bits[idx : idx + 3])
    idx += 3
    type_id = to_int(bits[idx : idx + 3])
    idx += 3
    match type_id:
        case 4:
            n = []
            cont = True
            while cont:
                n.extend(bits[idx + 1 : idx + 5])
                cont = bits[idx] == 1
                idx += 5
            args_stack.append(to_int(n))
        case other:
            length_type = bits[idx]
            idx += 1
            match length_type:
                case 0:
                    length = to_int(bits[idx:idx+15])
                    idx += 15
                case 1:
                    length = to_int(bits[idx:idx+11])
                    idx += 11
                case other:
                    print(f"invalid length type {other}")
                    exit(1)
            op_stack.append(type_id)
            new_info = [length, 0, length_type]
    if subpacket_info:
        info = subpacket_info[-1]
        if info[2] == 1:
                info[0] -= 1
        info[1] += 1
    for info in subpacket_info:
        if info[2] == 0:
            info[0] -= idx - strt
    if new_info:
        subpacket_info.append(new_info)

print(args_stack[0])
