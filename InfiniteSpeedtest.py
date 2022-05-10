# 通信容量無制限の携帯回線が本当に無制限か確認するためのコード
import subprocess

# 無限にダウンロードのみのスピードテストを実行(Ctrl-z以外に止める方法はないので注意して実行すること！)
while True:
    try:
        res = subprocess.check_call("speedtest --download", shell=True)
    except:
        print("error.")
