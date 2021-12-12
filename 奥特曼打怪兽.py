# 访问器—gettrt方法：@property
#修改器—setter方法：@(属性名).setter
#限定类绑定的属性：__slots__=('属性名'，'属性名'.....)属性之间用单引号引用，逗号隔开
#静态方法和类方法：@staticmethod
#类之间的关系：继承，关联（聚合/合成）和依赖
"""
使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用
@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。

"""
# other 指另一个类


#奥特曼打小怪兽
from abc import ABCMeta,abstractmethod
from random import randint,randrange

class Fighter(object,metaclass=ABCMeta):#metaclass=ABCMeta:只能被继承，而不能被实例化
    __slots__=('_name','_hp')
    def __init__(self,name,hp):
        self._name=name
        self._hp=hp
    @property #只读属性
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    @hp.setter #可以修改
    def hp(self,hp):
        self._hp=hp if hp>=0 else 0
    @property
    def alive (self):
        return self._hp > 0
    
    @abstractmethod #子类必须有这个方法，否则报错
    def attack(self,other):
        pass
    
class Ultraman(Fighter):
    __slots__=('_name','_hp','_mp')
        
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp=mp
            
    def attack(self,other):
        other.hp -= randint(15,25)
        
    def huge_attack(self,other):
        if self._mp >= 50:
            self._mp -=50
            injury =other.hp*3//4
            injury=injury if injury>=50 else 50
            other.hp -=injury
            return True
        else:
            self.attack(other)
            return False
        
    def magic_attack(self,others):
        if self._mp>=20:
            self._mp -=20
            for temp in others:
                if temp.alive:
                    temp.hp -=randint(15,20)
            return True
        else:
            return False
        
    def resume(self):
        incr_point=randint(1,10)
        self._mp +=incr_point
        return incr_point
        
    def __str__(self):
        return '~~~%s奥特曼~~~\n'%self._name+'生命值：%d\n'%self._hp+'魔法值：%d\n'%self._mp

    
class Monster(Fighter):
    __slots__=('_name','_hp')
    def attack(self,other):
        other.hp -=randint(10,20)
    
    def __str__(self):
        return "~~~%s小怪兽~~~\n"%self._name+'生命值：%d\n'%self._hp
    

def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive>0:
            return True
    return False

def select_alive_one(monsters):
    monsters_len=len(monsters)
    while True:
        index=randrange(monsters_len)
        monster=monsters[index]
        if monster.alive>0:
            return monster

def display_info(ultraman,monsters):
    print(ultraman)
    for monster in monsters:
        print(monster,end='')
        
def main():
    u= Ultraman('孙悟空',1000,120)
    m1=Monster('六耳猕猴',900)
    m2=Monster('如来佛祖',1500)
    m3 =Monster('太上老君',1200)
    ms=[m1,m2,m3]
    fight_round=1
    while u.alive and is_any_alive(ms):
        print("------第%02d回合-------"%fight_round)
        m=select_alive_one(ms)
        skill=randint(1,10)
        if skill<=6:
            print("%s使用普通攻击打了%s."%(u.name,m.name))
            u.attack(m)
            print("%s的魔法值恢复了%d点."%(u.name,u.resume()))
        elif skill<= 9:
            if u.magic_attack(ms):
                print("%s使用了魔法攻击。"%u.name)
            else:
                print("%s使用魔法攻击失败"%u.name)
        else :
            if u.huge_attack(m):
                print('%s使用究极必杀技打了%s.'%(u.name,m.name))
            else:
                print('%s使用普通攻击打了%s.'%(u.name,m.name))
                print('%s的魔法值恢复了%d点'%(u.name,u.resume()))
        if m.alive>0:
            print("%s回击了%s."%(m.name,u.name))
            m.attack(u)
        display_info(u,ms)
        fight_round+=1
    print('-----战斗结束！--------\n')
    if u.alive>0:
        print("%s奥特曼胜利！"%u.name)
    else:
        print('小怪兽胜利！')
        
if __name__=='__main__':
    main()
