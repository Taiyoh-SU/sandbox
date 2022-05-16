from math import sqrt
from decimal import Decimal, ConversionSyntax, InvalidOperation
import re


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


def decimal_change(n):
    try:
        return Decimal(n)
    except InvalidOperation:
        print(f'"{n}" is not a number.')
        return 0


def is_decimal(n):
    try:
        Decimal(n)
    except InvalidOperation:
        return False
    else:
        return True


a = Decimal("0")
memory = []
is1commandlist = ["p", "s", "m", "d", "+", "-", "*", "/", "power", "^", "%"]
while True:
    print(
        f"{pycolor.CYAN}{a }{pycolor.END}\n{pycolor.ACCENT}❯{pycolor.END} ", end="",
    )
    try:
        input_string = input().split()
        input_string[0] = input_string[0]
    except EOFError:
        print(pycolor.RED + "\nEOF has been entered." + pycolor.END)
        break
    except KeyboardInterrupt:
        print(pycolor.RED + "\nA KeyBoardInterrupt occurred." + pycolor.END)
        break
    except IndexError:
        print("Index Error.")
        continue

    if input_string[0] == "exit":
        print(pycolor.GREEN + "Bye." + pycolor.END)
        break

    if input_string[0] in is1commandlist:
        try:
            input_string[1] = input_string[1]
        except IndexError:
            print("Index Error.")
        pl = re.split("[+]", input_string[1])
        mi = re.split("[-]", input_string[1])
        mu = re.split("[*]", input_string[1])
        di = re.split("[/]", input_string[1])
        if len(pl) == 2:
            input_string[1] = Decimal(pl[0]) + Decimal(pl[1])
        elif len(mi) == 2:
            input_string[1] = Decimal(mi[0]) - Decimal(mi[1])
        elif len(mu) == 2:
            input_string[1] = Decimal(mu[0]) * Decimal(mu[1])
        elif len(di) == 2:
            input_string[1] = Decimal(di[0]) / Decimal(di[1])

    if input_string[0] == "p" or input_string[0] == "+":
        try:
            a += decimal_change(input_string[1])
        except IndexError:
            print("Index Error.")

    elif input_string[0] == "s" or input_string[0] == "-":
        try:
            a -= decimal_change(input_string[1])
        except IndexError:
            print("Index Error.")

    elif input_string[0] == "m" or input_string[0] == "*":
        try:
            a *= decimal_change(input_string[1])
        except IndexError:
            print("Index Error.")

    elif input_string[0] == "d" or input_string[0] == "/":
        try:
            a /= decimal_change(input_string[1])
        except ZeroDivisionError:
            print("Zero Division Error.")
        except IndexError:
            print("Index Error.")

    elif input_string[0] == "^" or input_string[0] == "power":
        try:
            a = a ** decimal_change(input_string[1])
        except IndexError:
            print("Index Error.")

    elif input_string[0] == "%":
        try:
            a *= decimal_change(input_string[1]) / Decimal("100")
        except IndexError:
            print("Index Error.")

    elif input_string[0] == "sqrt":
        a = sqrt(a)

    elif input_string[0] == "c":
        a = 0

    elif input_string[0] == "save":
        memory.append(a)
        print(f"{pycolor.BLUE}Saved {a}.{pycolor.END}")

    elif input_string[0] == "load":
        if not memory:
            print("No saved results.")
            continue
        print("Select the results.")
        for i, item in enumerate(memory):
            print(f"{i}:{item}")
        b = input("Index:")
        try:
            b = int(b)
            print(f"{pycolor.BLUE}Loaded {memory[b]}{pycolor.END}.")
        except ValueError:
            print(f'"{b}" is not a number.')
        except IndexError:
            print("Index Error.")
        else:
            a = memory[b]

    elif a == 0 and is_decimal(input_string[0]):
        a = Decimal(input_string[0])

    else:
        print(
            pycolor.PURPLE
            + "Error: command not found\nList of Commands:p, s, m, d, power, sqrt, +, -, /, *, ^, %, save, load, c, exit."
            + pycolor.END
        )


"""
コマンドライン計算機
使用方法:[コマンド] [数値(一部不必要)]
+,p:後ろに入力した数値を足します。
-,s:後ろに入力した数値を引きます。
*,m:後ろに入力した数値をかけます。
/,d:後ろに入力した数値で割ります。
^,power:「今までの結果」の「入力した数値」乗を出します
%:「今までの結果」の「入力した数値」パーセントを出します。
sqrt:今までの結果の平方根を出します。
save:今までの結果を保存します。
load:今までの保存した結果を読み込みます。
c:今までの結果を0にします。
exit:終了します。

更新履歴
v1.0.0:四則演算,c,exit実装
v1.0.1:power,sqrt実装
v1.0.2:save,load実装
v1.1:精度の観点からDecimalモジュールを使うように変更。
v1.1.2:+-*/^の5つを後ろでも使えるように変更。
v1.1.3:%を実装。
v1.1.4:loadのバグ修正。
"""
