
x = 7
y = 2

a = 0.45
b = 0.35
c = 0.1

class TestClass:

    def test_float1(self):
        assert type(x/y) == float

    # Негативный тест на тип данных float
    # Должно было получиться 0, но так как это float, то 0 не получится
    def test_float2(self):
        assert (a - b - c) != 0

