def запросить_информацию(сообщение):
    ответ_пользователя = input(сообщение)
    return ответ_пользователя
def кнбяс():
    class Игрок:
        def __init__(self, пр_имя) -> None:
            self.имя = пр_имя
            self.счет = 0
    
   
    юзер = Игрок(запросить_информацию("Пожалуйста, введите своё имя перед началом игры: "))
    комп = Игрок("Леонард")

    ДОПУСТИМЫЕ_КОМАНДЫ = ["К","Н","Б","Я","С","СБРОС","ВЫХОД"]

    команда = запросить_информацию("Введите команду: ")
    if команда in ДОПУСТИМЫЕ_КОМАНДЫ:
        print ("Продолжение следует!")