import math

class Vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_scalar(cls, scalar):
        if isinstance(scalar, float) or isinstance(scalar, int):
            return Vec3(x=scalar, y=scalar, z=scalar)
        else:
            return NotImplemented

    @property
    def r(self):
        return self.x

    @property
    def g(self):
        return self.y

    @property
    def b(self):
        return self.z

    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(x=self.x+other.x,
                        y=self.y+other.y,
                        z=self.z+other.z)
        elif isinstance(other, float) or isinstance(other, int):
            return Vec3(x=self.x+other,
                        y=self.y+other,
                        z=self.z+other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3(x=self.x-other.x,
                        y=self.y-other.y,
                        z=self.z-other.z)
        elif isinstance(other, float) or isinstance(other, int):
            return Vec3(x=self.x-other,
                        y=self.y-other,
                        z=self.z-other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(x=self.x*other.x,
                        y=self.y*other.y,
                        z=self.z*other.z)
        elif isinstance(other, float) or isinstance(other, int):
            return Vec3(x=self.x*other,
                        y=self.y*other,
                        z=self.z*other)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Vec3):
            return Vec3(x=self.x/other.x,
                        y=self.y/other.y,
                        z=self.z/other.z)
        elif isinstance(other, float) or isinstance(other, int):
            return Vec3(x=self.x/other,
                        y=self.y/other,
                        z=self.z/other)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Vec3):
            self.x+=other.x
            self.y+=other.y
            self.z+=other.z
            return self
        elif isinstance(other, float) or isinstance(other, int):
            self.x+=other
            self.y+=other
            self.z+=other
            return self
        else:
            return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Vec3):
            self.x-=other.x
            self.y-=other.y
            self.z-=other.z
            return self
        elif isinstance(other, float) or isinstance(other, int):
            self.x-=other
            self.y-=other
            self.z-=other
            return self
        else:
            return NotImplemented

    def __imul__(self, other):
        if isinstance(other, Vec3):
            self.x*=other.x
            self.y*=other.y
            self.z*=other.z
            return self
        elif isinstance(other, float) or isinstance(other, int):
            self.x*=other
            self.y*=other
            self.z*=other
            return self
        else:
            return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, Vec3):
            self.x/=other.x
            self.y/=other.y
            self.z/=other.z
            return self
        elif isinstance(other, float) or isinstance(other, int):
            self.x/=other
            self.y/=other
            self.z/=other
            return self
        else:
            return NotImplemented

    def __neg__(self):
        return Vec3(x=-self.x, y=-self.y, z=-self.z)

    def cross(self, other):
        if isinstance(other, Vec3):
            return Vec3(x=(self.y*other.z)-(self.z*other.y),
                        y=(self.z*other.x)-(self.x*other.z),
                        z=(self.x*other.y)-(self.y*other.x))
        else:
            return NotImplemented

    def dot(self, other):
        if isinstance(other, Vec3):
            return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
        else:
            return NotImplemented

    def length(self):
        return math.sqrt(self.squared_length())

    def squared_length(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def unit_vector(self):
        return self / self.length()
