from pathlib import Path

with open(Path(__file__).with_name("input")) as fp:
    inp = fp.read().strip()


def add(x, y):
    return [x] + [y]


class TryAgain(Exception):
    pass


def reduce(n):
    try:
        _reduce_explode(n, [])
        _reduce_split(n, [])
    except TryAgain:
        reduce(n)


def _stack_idx(n, stack):
    for i in stack:
        n = n[i]
    return n


def _add(n, v, d):
    while isinstance(n[d], list):
        n = n[d]
    n[d] += v


def _or(a, b):
    return a or b


def _explode(n, stack):
    last = stack[-1]
    pair = _stack_idx(n, stack[:-1])
    while _or(ll := isinstance(pair[0], list), rl := isinstance(pair[1], list)):
        if ll and all(isinstance(p, list) for p in pair[0]):
            pair = pair[0]
        elif rl and all(isinstance(p, list) for p in pair[1]):
            pair = pair[1]
        else:
            break
    l, r = pair[last]
    pair[last] = 0
    other = not last
    if other:
        o = r
        v = l
    else:
        o = l
        v = r
    if isinstance(pair[other], int):
        pair[other] += o
    else:
        _add(pair[other], o, not other)
    curr = n
    nodestack = []
    for i in stack[:-1]:
        nodestack.append(curr)
        curr = curr[i]
    for node, idx in zip(nodestack[::-1], stack[-2::-1]):
        if idx == other:
            if isinstance(node[not other], int):
                node[not other] += v
            else:
                _add(node[not other], v, other)
            break


def _split(n, stack):
    last = stack[-1]
    pair = _stack_idx(n, stack[:-1])
    v = pair[last] / 2
    l = int(v)
    r = round(v + 0.0001)
    pair[last] = [l, r]


def _reduce_explode(n, stack):
    if len(stack) == 4:
        _explode(n, stack)
        raise TryAgain from None
    for i in (0, 1):
        stack.append(i)
        curr = _stack_idx(n, stack)
        if isinstance(curr, list):
            _reduce_explode(n, stack)
        stack.pop()


def _reduce_split(n, stack):
    for i in (0, 1):
        stack.append(i)
        curr = _stack_idx(n, stack)
        if isinstance(curr, int):
            if curr >= 10:
                _split(n, stack)
                raise TryAgain from None
        else:
            _reduce_split(n, stack)
        stack.pop()


def magnitude(n):
    if isinstance(n, int):
        return n
    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])


nums = []

for line in inp.splitlines():
    nums.append(eval(line))


nums.reverse()
curr = nums.pop()

for num in nums[::-1]:
    curr = add(curr, num)
    reduce(curr)

print(magnitude(curr))
