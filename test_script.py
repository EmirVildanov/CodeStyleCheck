from collections import Callable


class Test:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def test_function(self):
        self.val1 += 2


class AnotherTest(Test)   :
    def __init__(self,  val1, val2, val3):
        super().__init__(val1, val2)
        self.val3 = val3

class test_class_With_strangeName:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
#comment in the center of file?
class TestClassWithBadParent(Callable):
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2


def test_classes_function():
    test = Test(3, 5)
    print(f'Test before is {test}')
    test.test_function()
    print(f'Test after is {test}')
    another_test = AnotherTest(4, 2, 1)
    print(f"Another test is {another_test}")
    print("One string" + 'another string')

def CHeckIfNumber_odd(number: int):
    if number == 0:
        return True
    elif number == 2:
        return True
    elif number == 4:
        return True
    elif number == 6:
        return True
    elif number == 8:
        return True
    elif number == 10:
        return True
    return False

def raise_many_exceptions(number: int):
    if number == 1:
        raise ValueError("1")
    if number == 2:
        raise ValueError("2")
    if number == 3:
        raise ValueError("3")
    if number == 4:
        raise ValueError("4")
    if number == 5:
        raise ValueError("5")

#comment in the end of file?