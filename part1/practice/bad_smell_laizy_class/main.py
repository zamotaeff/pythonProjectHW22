# Один из классов не делает совсем ничего,
# просто переадресует вызовы к другому классу.
# Удалите этот класс и перенаправьте вызовы напрямую.

class Unit:
    def __init__(self):
        self.x = 0
        self.y = 0

    def attack(self):
        pass

    def defense(self):
        pass

    def move(self, field: Field):
        field.set_unit(x=self.x, y=self.y, unit=self)


class Field:
    def set_unit(self, x, y, unit: Unit):
        pass

    def set_unit(self, x, y, unit: Unit):
        self.set_unit(x, y, unit)


class Main:
    def __init__(self):
        self.field = Field()
        self.unit = Unit()
        self.unit.move(field=self.field)
