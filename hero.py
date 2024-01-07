class SuperHero:
    people='people'
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def a(self):
        print(self.name)
    def hi(self):
        print(self.health_points*2)
    def __str__(self):
        return (f'Nick: {self.nickname}, SuperPower: {self.superpower}, Health_Point: {self.health_points}')
    def __len__(self):
        return len(self.catchphrase)

Hero = SuperHero('Ибрагим', 'Ями', 'магия тьмы', 100, 'здесь я превзайду свои лимиты')
Hero.a()
print(Hero)
print(len(Hero))
Hero.hi()

