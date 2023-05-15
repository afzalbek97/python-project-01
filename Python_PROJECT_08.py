#unit 33 심사문
i = n+1
    def minus():
        nonlocal i
        i -= 1
        return i
    return minus

    #unit 34 심사문
    class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    
    def tibbers(self):
        print('티버: 피해량 {0}'.format(self.ability_power * 0.65 + 400))


    #unit 35 심사문
    @classmethod
def from_string(cls,time_string):
    hour,minutes,second=map(int,time_string.split(':'))
    time=cls(hour,minute,second)
    return time
    
    @staticmethot
    def is_time_valid(time_string):
        hour,minute,second=map(int,time_string.split(':'))
        return hour<=24 and minute<=59 and second<=60
    
    #unit 36 심사문
    class Bird(Animal, Wing):
    def fly(self):
        print('날다')
    