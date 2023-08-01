class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}さんは、20歳以上なので大人です。")
        else:
            print(f"{self.name}さんは、20歳未満なので大人ではありません。")


members = [
    Human("tanaka", 18),
    Human("mori", 21),
    Human("hayashi", 32),
    Human("matuo", 45),
    Human("koishi", 19),
]

for member in members:
    member.check_adult()
