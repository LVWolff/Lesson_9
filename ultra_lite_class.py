
class T_Class():

    def __init__(self, name):
        self.name_ob = name
        self.__hidden_propetice = name + ' (hidden)'

    def __str__(self):
        return 'Тестовый класс: ' + self.name_ob

    def __hiddem_method(self):
        print("Код выполняемый в скрытой функции класса")
        print("Скрытое свойство:", self.__hidden_propetice)

    def t_func(self):
        self.__hiddem_method()
        print('Код выполяемые в тестовом методе класса')



t_class = T_Class('test class 1')
print(t_class)
t_class.t_func()