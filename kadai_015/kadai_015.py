class Human:
    # コンストラクタ
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # メソッド
    def printinfo(self):
        print(f"名前は{self.name}で年齢は{self.age}歳です")


tanaka = Human("田中", "22")
tanaka.printinfo()
