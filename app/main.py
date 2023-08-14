from decimal import Decimal

class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other

        return self

    def __mul__(self, other: int) -> "Distance":
        if not isinstance(other, Distance):
            return Distance(self.km * other)

    def __truediv__(self, other: Decimal) -> "Distance":
        if not isinstance(other, Distance):
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: int) -> bool:
        return not (self.km < other) and self.km != other

    def __eq__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: int) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
