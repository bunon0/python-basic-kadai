list = [
    "月曜日は晴れです",
    "火曜日は雨です",
    "水曜日は晴れです",
    "木曜日は晴れです",
    "金曜日は曇りです",
    "土曜日は曇のち雨です",
    "日曜日は雷雨です",
]

dictionary = {
    "mon": "晴れ",
    "tue": "雨",
    "wed": "晴れ",
    "thu": "晴れ",
    "fri": "曇り",
    "sat": "曇のち雨",
    "sun": "雷雨",
}

print(f"配列から、{list[2]}")
print(f"連想配列から、水曜日は{dictionary['wed']}です")
