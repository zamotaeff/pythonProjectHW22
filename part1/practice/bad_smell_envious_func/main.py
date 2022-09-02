# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    @property
    def cube_volume(self):
        return self.get_x() * self.get_y() * self.get_z()


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.cube_volume
