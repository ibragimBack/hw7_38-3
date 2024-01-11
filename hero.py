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
        print(f"len_catchpharse: ",len(self.catchphrase))

Hero = SuperHero('Ибрагим', 'Ями', 'магия тьмы', 100, 'здесь я превзайду свои лимиты')
Hero.a()
print(Hero)
print(Hero.catchphrase)
Hero.__len__()
Hero.hi()



class Superman(SuperHero):
    hero = 'hero'
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage,fly=False):
        super(Superman, self).__init__(name,nickname,superpower,health_points,catchphrase)
        self.damage = damage
        self.fly = fly

    def hi(self):
        self.fly = True
        print(f"health: {self.health_points ** 2}")
    def get_info(self):
        print('True in the True_phrase')

hero2 = Superman('Кларк','Супермен','лазерный взгляд',1000,'Я - последний сын Криптона',500,True,)
hero2.a()
print(hero2)
print(hero2.catchphrase)
hero2.__len__()
hero2.hi()
hero2.get_info()



class Batman(SuperHero):
    hero2 = 'hero'
    def __init__(self,name,nickname,superpower,health_points,catchphrase,damage,fly=False):
        super(Batman, self).__init__(name,nickname,superpower,health_points,catchphrase)
        self.damage = damage
        self.fly = fly
    def hi(self):
        self.fly = True
        print(self.health_points ** 2)

    def get_info(self):
        print('True in the True_phrase')

hero3 = Batman('Питер','Человек паук','Паутина',100,'Тётя Мей',15,False)
hero3.a()
print(hero3)
print(hero3.catchphrase)
hero3.__len__()
hero3.hi()
hero3.get_info()



class Villain(Batman):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self,damage):
        print(f"damage: {self.damage ** 2}")

villain = Villain('Локи','Бог обмана','Магия',1000,'Я - Локи царь Асгарда',200,True)
villain.a()
print(villain)
print(villain.catchphrase)
villain.__len__()
villain.gen_x()
villain.crit(hero3.damage)


