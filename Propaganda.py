# ジョークプログラム
# 検閲（プロパガンダ）ソート
# コンセプト：O(1)のソートアルゴリズムを作りたい！
# 内容：リストを渡すと「この入力配列は法的な理由により削除されました。」と表示し，要素を消したソートを返す，要素数0なのでソートされているものとするためO(1)である


def censorship_sort(list):
    print("WARNING: This input array was deleted for legal reasons.")
    return []


list = [3, 4, 6, 1, 2, 5, 9, 8, 10, 7]
print(censorship_sort(list))
