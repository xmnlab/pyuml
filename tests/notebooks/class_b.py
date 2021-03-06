import dataclasses

from class_a import ClassA


@dataclasses.dataclass
class ClassB(ClassA):
    ba: str = None
    bb: int = 0

    def print_content(self):
        print(self.__dict__)


class ClassZ:
    def __init__(self, z: int):
        self.z = z

    def print_content_z(self):
        print(self.__dict__)
