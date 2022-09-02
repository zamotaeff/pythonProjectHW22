class Unit:

    def __init__(self, state: str, x: int, y: int, speed: float = 1.0):
        self.state = state
        self.x = x
        self.y = y
        self.speed = speed

    def move(self, direction: str, field: Field):
        speed = self._get_speed()

        if direction == 'UP':
            field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')


class Field:
    def __init__(self, x: int, y: int, unit: [Unit, ]):
        self.x = x
        self.y = y
        self.units = []

    def set_unit(self, x, y, unit: Unit):
        # Устанавливаем, что в этом поле будет наш юнит
        # Находим поле по координатам и добавляем в список units
        pass
