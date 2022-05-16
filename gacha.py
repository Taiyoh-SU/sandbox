import random


class pycolor:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RETURN = "\033[07m"  # 反転
    ACCENT = "\033[01m"  # 強調
    FLASH = "\033[05m"  # 点滅
    RED_FLASH = "\033[05;41m"  # 赤背景+点滅
    END = "\033[0m"


r = float(input("確率(%):")) / 100
u = int(input("キャラ数:"))
i = int(input("試行回数:"))
record = []


def once(r):
    count = 0
    while True:
        a = random.random()
        tf = (
            pycolor.RED + str(a < r) + pycolor.END
            if a < r
            else pycolor.BLUE + str(a < r) + pycolor.END
        )
        count += 1
        print(f"rand={a:.6f}, {tf}")
        if a < r:
            break
    return count


def multiple(r, num):
    rec = []
    for i in range(num):
        rec.append(once(r))
    return sum(rec)


for a in range(i):
    record.append(multiple(r, u))

print(f"{record}")
print(f"Average:{sum(record)/len(record)}")
print(f"Max:{max(record)}")
print(f"Min:{min(record)}")
