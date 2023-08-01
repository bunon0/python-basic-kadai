class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}さんは、20歳以上なので大人です。")
        else:
            print(f"{self.name}さんは、20歳未満なので大人ではありません。")


tanaka = Human("tanaka", 20)
tanaka.check_adult()

mori = Human("mori", 19)
mori.check_adult()
