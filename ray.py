from vec3 import Vec3

class Ray:
    def __init__(self, origin=Vec3(), direction=Vec3()):
        self.origin = origin
        self.direction = direction

    def point_at_parameter(self, target) -> Vec3:
        return self.origin + self.direction*target
