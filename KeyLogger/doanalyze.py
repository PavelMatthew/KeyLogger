from pynput.keyboard import Key, Listener
import time
from letter import Letter
import keyboard
import time

import keyboard
from pynput.keyboard import Key, Listener

from letter import Letter
from userdata import UserData
from writeanalyze import WriteAnalyze
from pprint import pprint


class DoAnalyze():

    def __init__(self, user_name):
        self.user_name = user_name
        self.text = []
        self.mistakes_counter = 0  # количество ошибок(backspace)
        self.dict_symbols = {}  # словарь символов с временем удержания
        self.middle_time_pressed = 0  # среднее время удержания клавиш
        self.s = 0
        self.n = 0
        self.dict_pauses = {}  # словарь пауз между клавищами (биграммы с временем)
        self.s2 = 0
        self.n2 = 0
        self.middle_pauses = 0

        self.middle_speed = 0  # среднее количество символов в минуту (скорость печатанья текста)

        self.dict_pauses_less_filter = {}  # словарь пауз между клавищами (биграммы с временем) с фильтром менее 1 сек
        self.s3 = 0
        self.n3 = 0
        self.middle_speed_without_pauses = 0

    def on_press(self, key):

        try:

            if len(str(key)) == 3:
                fl = str(key).lower()
                print(fl + "pressed")

                our_letter = Letter(fl, str(time.time()), str(0))
                self.text.append(our_letter)




            elif key == Key.backspace:
                if (len(self.text)) >= 1:
                    self.mistakes_counter = self.mistakes_counter + 1
                    le = len(self.text) - 1
                    self.text.pop(le)


            elif key == Key.space:
                our_letter = Letter(str(" "), str(time.time()), str(0))
                self.text.append(our_letter)

            elif key == Key.alt.f10:

                print("Сработало")
                # for i in range(0, len(self.text)):
                # let = self.text[i]
                # let.print_all()

                return False


        except:

            print("ОШИБКА В МЕТОДЕ on_pressed")

    def on_release(self, key):
        try:
            if len(self.text) > 0:
                our_letter = self.text[len(self.text) - 1]

                if len(str(key)) == 3:
                    print(f"{key} unpressed" + str(time.time()))

                    if str(our_letter.key_name) == str(key).lower() and len(self.text) > 0:
                        our_letter.unpressed_time = time.time()
                        l = len(self.text) - 1
                        self.text.pop(l)
                        self.text.append(our_letter)

                elif key == Key.space:
                    print(f"{key} unpressed" + str(time.time()))

                    if str(our_letter.key_name) == " " and len(self.text) > 0:
                        our_letter.unpressed_time = time.time()
                        l = len(self.text) - 1
                        self.text.pop(l)
                        self.text.append(our_letter)

        except:
            print(str(key) + " Ошибка в методе on_release")

    # метод возвращает текст без длительного зажатия клавиш

    def delete_for_pressed_filter(self, our_text_for_filter):

        len_text = len(our_text_for_filter)
        counter = len_text

        if len(our_text_for_filter) > 0:

            for i in range(0, len_text):

                counter = counter - 1
                letter_first_zero = our_text_for_filter[counter]
                if str(letter_first_zero.unpressed_time) == str("0"):
                    el_before = counter + 1
                    self.text[el_before].pressed_time = letter_first_zero.pressed_time
                    self.text.pop(counter)

        return our_text_for_filter

    def result_arr(self):

        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

        result_from_text = self.delete_for_pressed_filter(self.text)

        print("RESULT")
        for i in range(0, len(result_from_text)):
            # время удержания клавиш в секундах
            if str(result_from_text[i].key_name) in self.dict_symbols:
                self.dict_symbols[str(result_from_text[i].key_name)].append(
                    float(result_from_text[i].unpressed_time) - float(result_from_text[i].pressed_time))
                self.s = self.s + float(result_from_text[i].unpressed_time) - float(result_from_text[i].pressed_time)
                self.n = self.n + 1
            if (str(result_from_text[i].key_name) in self.dict_symbols) == False:
                self.dict_symbols[str(result_from_text[i].key_name)] = [
                    float(result_from_text[i].unpressed_time) - float(result_from_text[i].pressed_time)]
                self.s = self.s + float(result_from_text[i].unpressed_time) - float(result_from_text[i].pressed_time)
                self.n = self.n + 1

            # result_from_text[i].print_all()

        for i in range(0, len(result_from_text) - 1):
            # if (float(result_from_text[i+1].pressed_time)-float(result_from_text[i].unpressed_time)) < 1: #отсеиваем паузы больше 1 сек

            if (str(result_from_text[i].key_name) + str(result_from_text[i + 1].key_name)) in self.dict_pauses:
                self.dict_pauses[(str(result_from_text[i].key_name) + str(result_from_text[i + 1].key_name))].append(
                    (float(result_from_text[i + 1].pressed_time) - float(result_from_text[i].unpressed_time)))
                self.s2 = self.s2 + (
                            float(result_from_text[i + 1].pressed_time) - float(result_from_text[i].unpressed_time))
                self.n2 = self.n2 + 1

            if ((str(result_from_text[i].key_name) + str(
                    result_from_text[i + 1].key_name)) in self.dict_pauses) == False:
                self.dict_pauses[(str(result_from_text[i].key_name) + str(result_from_text[i + 1].key_name))] = [
                    (float(result_from_text[i + 1].pressed_time) - float(result_from_text[i].unpressed_time))]
                self.s2 = self.s2 + (
                            float(result_from_text[i + 1].pressed_time) - float(result_from_text[i].unpressed_time))
                self.n2 = self.n2 + 1
        for i in range(0, len(result_from_text) - 1):

            if (float(result_from_text[i + 1].pressed_time) - float(
                    result_from_text[i].unpressed_time)) < 1:  # отсеиваем паузы больше 1 сек

                if (str(result_from_text[i].key_name) + str(
                        result_from_text[i + 1].key_name)) in self.dict_pauses_less_filter:
                    self.dict_pauses_less_filter[
                        (str(result_from_text[i].key_name) + str(result_from_text[i + 1].key_name))].append(
                        (float(result_from_text[i + 1].pressed_time) - float(result_from_text[i].unpressed_time)))
                    self.s3 = self.s3 + (
                                float(result_from_text[i + 1].pressed_time) - float(result_from_text[i].unpressed_time))
                    self.n3 = self.n3 + 1

                if ((str(result_from_text[i].key_name) + str(
                        result_from_text[i + 1].key_name)) in self.dict_pauses_less_filter) == False:
                    self.dict_pauses_less_filter[
                        (str(result_from_text[i].key_name) + str(result_from_text[i + 1].key_name))] = [
                        (float(result_from_text[i + 1].pressed_time) - float(result_from_text[i].unpressed_time))]
                    self.s3 = self.s3 + (
                                float(result_from_text[i + 1].pressed_time) - float(result_from_text[i].unpressed_time))
                    self.n3 = self.n3 + 1

        # print("MISTAKES")
        # print("Кол-во ошибок:" + str(self.mistakes_counter))

        # print(self.dict_symbols)
        self.middle_time_pressed = (self.s / self.n)
        # print("Среднее время удержания клавиш: " + str(self.s/self.n))
        # print(self.dict_pauses)
        self.middle_pauses = (self.s2 / self.n2)
        # print("Среднее время пауз меньших 1 сек: " + str(self.s2/self.n2))
        self.middle_speed = (60 / ((self.s + self.s2) / (self.n + self.n2)))
        # print("Среднея скорость набора текста без вычета пауз: "+str(60/((self.s+self.s2)/(self.n+self.n2))))
        self.middle_speed_without_pauses = (60 / ((self.s + self.s3) / (self.n + self.n3)))
        # print("Среднея скорость набора текста c вычетом  пауз > 1 : " + str(60 / ((self.s + self.s3) / (self.n + self.n3))))

        final_text = []
        for i in range(len(self.text)):
            a = str(self.text[i].key_name)
            b = a.replace("'", "")
            # print(b)
            final_text.append(b)

        ou = UserData(self.user_name, final_text, self.mistakes_counter, self.middle_time_pressed, self.middle_speed,
                      self.middle_speed_without_pauses, self.dict_symbols, self.dict_pauses)
        # print(ou.__dict__)
        wa = WriteAnalyze(ou)
        wa.write_to_file()
        # pprint(fw.read_file())

