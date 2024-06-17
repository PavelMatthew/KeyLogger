from filework import FileWork
from writeanalyze import WriteAnalyze
from pprint import pprint
from statistics import mode

class Analizator:

    def __init__(self):
        self.analyze_dict = WriteAnalyze.read_file()
        self.data_dict = FileWork.read_file()

        #self.u_n = ""
        self.txt = ""
        self.n_m = 0
        self.m_t_p = 0
        self.m_s = 0
        self.m_s_w_b_p = 0
        self.d_s = 0
        self.d_p = 0

        self.analyze_dict_without_arr = {}
        self.analyze_dict_pauses_without_arr = {}
        self.total_analyze = []


    def tanimoto(self,s1, s2):
        a, b, c = len(s1), len(s2), 0.0

        for sym in s1:
            if sym in s2:
                c += 1

        return c / (a + b - c)

    def find_txt(self):
        l = len(self.data_dict['users'])
        #print(l)
        #print(''.join(self.analyze_dict['users'][0]['text']))
        at = ''.join(self.analyze_dict['users'][0]['text'])
        #print("!!!")

        supportive = 0
        from_user = 0
        for key in self.data_dict['users']:
            #print(key['user_name'])
            #print(self.tanimoto(at, ''.join(key['text'])))
            if self.tanimoto(at, ''.join(key['text'])) > supportive:
                supportive = self.tanimoto(at, ''.join(key['text']))
                from_user = self.data_dict['users'].index(key)


            else:
                continue
        #print(from_user)
        #print(''.join(key['text']))
        #print(supportive)

        self.txt = "Наибольшое совпадение по тексту с пользователем: " + str(self.data_dict['users'][from_user]['user_name']) + ",\nсоставляет " + str(supportive*100) + "%"
        self.total_analyze.append(str(self.data_dict['users'][from_user]['user_name']))
        return self.txt

    def find_n_m(self):

        supportive = 1000
        from_user = 0
        for key in self.data_dict['users']:

            if supportive >= abs(key['num_mistake'] - self.analyze_dict['users'][0]['num_mistake']):
                supportive = abs(key['num_mistake'] - self.analyze_dict['users'][0]['num_mistake'])
                from_user = self.data_dict['users'].index(key)
            else:
                continue


        self.n_m = "\n Наибольшое совпадение по кол-ву ошибок с пользователем: " + str(self.data_dict['users'][from_user]['user_name']) + ", \nотклонение составляет  " + str(supportive)
        self.total_analyze.append(str(self.data_dict['users'][from_user]['user_name']))
        return self.n_m

    def find_m_t_p(self):
        supportive = 1000.0
        from_user = 0
        for key in self.data_dict['users']:

            if supportive >= abs(float(key['middle_time_pressed']) - float(self.analyze_dict['users'][0]['middle_time_pressed'])):
                supportive = abs(float(key['middle_time_pressed']) - float(self.analyze_dict['users'][0]['middle_time_pressed']))
                #print(supportive)
                from_user = self.data_dict['users'].index(key)
            else:
                continue


        self.m_t_p = "Наибольшое совпадение по среднему удержанию клавиш: " + str(self.data_dict['users'][from_user]['user_name']) + ", отклонение составляет " + str(supportive)
        self.total_analyze.append(str(self.data_dict['users'][from_user]['user_name']))
        return self.m_t_p

    def find_m_s(self):
        supportive = 1000.0
        from_user = 0
        #print((self.analyze_dict['users'][0]['middle_speed']))

        for key in self.data_dict['users']:
            #print(float(key['middle_speed']))
            if supportive >= abs(float(key['middle_speed']) - float(self.analyze_dict['users'][0]['middle_speed'])):
                supportive = abs(float(key['middle_speed']) - float(self.analyze_dict['users'][0]['middle_speed']))

                from_user = self.data_dict['users'].index(key)
            else:
                continue


        self.m_s = "Наибольшое совпадение по средней скорости набора текста: " + str(self.data_dict['users'][from_user]['user_name']) + ",\n отклонение составляет " + str(supportive)
        self.total_analyze.append(str(self.data_dict['users'][from_user]['user_name']))
        return self.m_s

    def find_m_s_w_b_p(self):
        supportive = 1000.0
        from_user = 0
        #print((self.analyze_dict['users'][0]['middle_speed']))

        for key in self.data_dict['users']:
            #print(float(key['middle_speed']))
            if supportive >= abs(float(key['middle_speed_without_big_pauses']) - float(self.analyze_dict['users'][0]['middle_speed_without_big_pauses'])):
                supportive = abs(float(key['middle_speed_without_big_pauses']) - float(self.analyze_dict['users'][0]['middle_speed_without_big_pauses']))

                from_user = self.data_dict['users'].index(key)
            else:
                continue


        self.m_s_w_b_p = "Наибольшое совпадение по средней скорости набора текста без длительных пауз: " + str(self.data_dict['users'][from_user]['user_name']) + ",\nотклонение составляет " + str(supportive)
        self.total_analyze.append(str(self.data_dict['users'][from_user]['user_name']))
        return self.m_s_w_b_p

    def find_analyze_dict(self):
        ad = self.analyze_dict['users'][0]['dict_symbols']


        for key in ad:

            sum2 = 0
            n2 = 0
            for i in ad[key]:
               sum2 = sum2 + float(i)
               n2 = n2 + 1

            self.analyze_dict_without_arr[key] = sum2/n2
        return self.analyze_dict_without_arr


    
    def find_d_s(self):
        dd = self.data_dict['users']
        ad = self.find_analyze_dict()
        adwa = self.analyze_dict_without_arr
        #print(adwa)
        #print(self.analyze_dict['users'][0]['text'])

        the_smallest_dis = []
        the_name = " "
        for k in dd:

            ddhelp = {}
            for l in k['dict_symbols']:

                sum = 0
                n = 0
                for m in k['dict_symbols'][l]:
                    sum = sum + m
                    n = n +1
                ddhelp[l] = sum/n
            #print(ddhelp)

            sum_dis = 0
            num_dis = 0
            for m in ad:
                if m in ddhelp:
                    d = abs(ad[m] - ddhelp[m])
                    #print(d)
                    #print(ad[m])
                    #print(ddhelp[m])
                    #print("!!!!!!!!!!!!!!!!!!!!")
                    sum_dis = sum_dis + d
                    num_dis = num_dis + 1


            try :
                dis = sum_dis / num_dis
                the_smallest_dis.append(dis)

            except:
                pass
                #print("дел на 0")
           # print("---------------------")
        the_smallest_el = min(the_smallest_dis)
        o = the_smallest_dis.index(the_smallest_el)
        self.total_analyze.append(str(self.data_dict['users'][o]['user_name']))
        return 'Наибольшее совпадение по длительности нажатия с '+str(self.data_dict['users'][o]['user_name']) + '\n дисперсия по нажатиям: '+str(the_smallest_el)

    def find_analyze_dict_pauses(self):
        ad = self.analyze_dict['users'][0]['dict_pauses']


        for key in ad:

            sum2 = 0
            n2 = 0
            for i in ad[key]:
               sum2 = sum2 + float(i)
               n2 = n2 + 1

            self.analyze_dict_pauses_without_arr[key] = sum2/n2
        return self.analyze_dict_pauses_without_arr

    def find_d_p(self):
        dd = self.data_dict['users']
        ad = self.find_analyze_dict_pauses()
        #adwa = self.analyze_dict_without_arr
        #print(adwa)
        #print(self.analyze_dict['users'][0]['text'])

        the_smallest_dis = []
        the_name = " "
        for k in dd:

            ddhelp = {}
            for l in k['dict_pauses']:

                sum = 0
                n = 0
                for m in k['dict_pauses'][l]:
                    sum = sum + m
                    n = n +1
                ddhelp[l] = sum/n
            #print(ddhelp)

            sum_dis = 0
            num_dis = 0
            for m in ad:
                if m in ddhelp:
                    d = abs(ad[m] - ddhelp[m])
                    #print(d)
                    #print(ad[m])
                    #print(ddhelp[m])
                    #print("!!!!!!!!!!!!!!!!!!!!")
                    sum_dis = sum_dis + d
                    num_dis = num_dis + 1


            try :
                dis = sum_dis / num_dis
                the_smallest_dis.append(dis)

            except:
                pass
                #print("дел на 0")
            #print("---------------------")
        the_smallest_el = min(the_smallest_dis)
        o = the_smallest_dis.index(the_smallest_el)
        self.total_analyze.append(str(self.data_dict['users'][o]['user_name']))
        return 'Наибольшое совпадение по паузам с '+str(self.data_dict['users'][o]['user_name']) +'\n дисперсия по биграммам: '+ str(the_smallest_el)

    def most_common(self):
            return str(mode(self.total_analyze))


if __name__ == "__main__":

    a = Analizator()
    #print(a.find_txt())
    #print(a.find_n_m())
    #print(a.find_m_t_p())
    #print(a.find_m_s())
    #print(a.find_m_s_w_b_p())
    #print(a.find_d_p())
    #a.find_analyze_dict()





