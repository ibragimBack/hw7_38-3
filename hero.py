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



class Superman(SuperHero):
    hero = 'hero'
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage,fly=False):
        super(Superman, self).__init__(name,nickname,superpower,health_points,catchphrase)
        self.damage = damage
        self.fly = fly

    def hi(self):
        super().hi()
        print(self.health_points ** 2)
        self.fly = True
    def get_info(self):
        print('True in the True_phrase')

hero2 = Superman('Кларк','Супермен','лазерный взгляд',1000,'я не знаю какая у него фраза',500,True,)
# Superman.hi()
# Superman.get_info()
print(hero2)



class Batman(SuperHero):
    hero2 = 'hero'
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage,fly=False):
        super(Batman, self).__init__(name,nickname,superpower,health_points,catchphrase)
        self.damage = damage
        self.fly = fly
    def hi(self):
        super().hi()
        print(self.health_points ** 2)
        self.fly = True

    def get_info(self):
        print('True in the True_phrase')

hero3 = Batman('Питер','Человек паук','Паутина',100,'Тётя Мей',15,False)
# Batman.get_info()
# Batman.hi()
print(hero3)



class Villain(Batman):
    monster = 'monster'

    def gen_x(self):...

    def crit(self):
        print(self.damage ** 2)


