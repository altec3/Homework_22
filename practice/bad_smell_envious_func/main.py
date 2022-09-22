class Cube:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_volume(self):
        return self._x * self._y() * self._z()


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube: Cube):
        return cube.get_volume()
