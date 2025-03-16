# ファイル名: hello.py
# 作成者: 長田賢一郎
# 作成日: 2024/01/09
# 著作権: © 2024 OSAKEN.AI
#
# 説明:
# これは私の最初のPythonプログラムです。
# シンプルな挨拶を出力します。
#
# 更新履歴:
# 2024/01/09 - 初版作成


print("こんにちは、Pythonです。")
from datetime import datetime
print("--------------------------------")
current_time = datetime.now()
print(f"実行日時: {current_time.strftime('%Y年%m月%d日 %H:%M:%S')}")
print("--------------------------------")

