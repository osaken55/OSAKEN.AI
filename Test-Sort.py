"""
作成者：長田賢一郎
作成日：2024年3月27日
内容：2桁の乱数を50個生成し、降順で並べ替えるプログラム
"""

import random

# 2桁の数字を50個生成してリストに格納
numbers = [random.randint(10, 99) for _ in range(50)]

# 生成した数字を表示
print("生成された数字:")
print(numbers)

# 大きい順（降順）に並べ替え
sorted_numbers = sorted(numbers, reverse=True)

# 並べ替えた結果を表示
print("\n大きい順に並べ替えた数字:")
print(sorted_numbers)
