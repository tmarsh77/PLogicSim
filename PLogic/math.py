class Math:
    @staticmethod
    def lerp(v1, v2, t):
        return v1 + (v2 - v1) * t

    @staticmethod
    def get_cubic_bezier_point(p1, p2, p3, p4, t):
        raise NotImplemented

    @staticmethod
    def remap(value, a1, a2, b1, b2):
        return ((value - a1) / (a2 - a1)) * (b2 - b1) + b1

    @staticmethod
    def clamp(val, vmin, vmax):
        return max(min(vmax, val), vmin)
