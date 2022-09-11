import pytest

@pytest.mark.parametrize("digit,text", [("92222222222", "Petya"),("91111111111", "Ket")])
class TestClass:

#Функция проверяет, что digit содержит только числа, а text не выходит за ограничения поля 10 символов
    def test_str1(self, digit, text):
        assert digit.isdigit() & len(text) < 10

#Функция проверяет, что номер начинается с 9-ки (актуально для формы ввода номера телефона)
    def test_str2(self, text, digit):
       assert digit.find('9') == 0









