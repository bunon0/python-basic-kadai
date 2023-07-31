price1 = 100
price2 = 200
# taxをグローバルスコープへ変更
tax = 1.1


def total():
    return price1 + price2


print(total() * tax)
