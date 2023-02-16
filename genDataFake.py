import requests
import random
GoogleURL = 'https://docs.google.com/forms/d/e/1FAIpQLSdHkcm6aM210T2G9gTo_zkQjS29Y9aIQXMtGQwPNK0EKgs5rg'

urlResponse = GoogleURL+'/formResponse'
urlReferer = GoogleURL+'/viewform'

GenderList = ['Мужчина'] * 38 + ['Женщина'] * 62
AgeList = ['18 – 25'] * 9 + ['26 – 35'] * 21 + ['36 – 45'] * 44 + ['46 – 60'] * 25 + ['60+']
EduList = ['Основное общее образование'] + ['Среднее профессиональное образование'] * 41 + ['Бакалавриат'] * 57 + ['Магистратура']
WorkList = ['Работаю'] * 52 + ['Не работаю'] * 23 + ['Самозанятой'] * 25
IncomeList = ['До 3 млн UZS'] * 41 + ['3 – 5 млн UZS'] * 37 + ['5 – 10 млн UZS'] * 21 + ['10 – 30 млн UZS'] + ['От 30 млн UZS']
FreqList = ['Не покупаю'] * 4 + ['По необходимости'] * 87 + ['Реже чем раз в месяц'] * 4 + ['1 раз в месяц'] * 4 + ['1+ раз в две недели']
UndList = ['Полностью понимаю'] * 16 + ['Понимаю'] * 30 + ['Не уверен(на)'] * 20 + ['Скорее не понимаю'] * 20 + ['Нет понимаю'] * 14
AggList = ['Согласен'] * 20 + ['Не уверен'] * 43 + ['Не согласен'] * 37
# ImpList = ['Производитель','Мое знание о лекарстве','Прошлый опыт использования','Наличие в запасе (лекарство доступно для покупки в любой момент времени)','Наличие в разных местах (лекарство можно купить в большом количестве мест)','Цена','Мнение близких людей','Мнение специалистов (врачи/аптекари и т.п.)','Общественное мнение и мнение инфлюенсеров (знаменитости, блогеры)','Реклама лекарства','Дизайн упаковки']


ChoiceList1 = ['Полностью согласен'] * 30 + ['Согласен'] * 46 + ['Не уверен'] * 16 + ['Не согласен'] * 7 + ['Категорически не согласен']
ChoiceList2 = ['Полностью согласен'] * 18 + ['Согласен'] * 35 + ['Не уверен'] * 25 + ['Не согласен'] * 18 + ['Категорически не согласен'] * 4
ChoiceList3 = ['Полностью согласен'] * 29 + ['Согласен'] * 23 + ['Не уверен'] * 22 + ['Не согласен'] * 12 + ['Категорически не согласен'] * 14
ChoiceList4 = ['Полностью согласен'] * 39 + ['Согласен'] * 23 + ['Не уверен'] * 14 + ['Не согласен'] * 14 + ['Категорически не согласен'] * 10
ChoiceList5 = ['Полностью согласен'] * 29 + ['Согласен'] * 34 + ['Не уверен'] * 23 + ['Не согласен'] * 10 + ['Категорически не согласен'] * 4
ChoiceList6 = ['Полностью согласен'] * 15 + ['Согласен'] * 25 + ['Не уверен'] * 34 + ['Не согласен'] * 16 + ['Категорически не согласен'] * 10
ChoiceList7 = ['Полностью согласен'] * 18 + ['Согласен'] * 27 + ['Не уверен'] * 20 + ['Не согласен'] * 14 + ['Категорически не согласен'] * 21
ChoiceList8 = ['Полностью согласен'] * 27 + ['Согласен'] * 18 + ['Не уверен'] * 18 + ['Не согласен'] * 23 + ['Категорически не согласен'] * 14
ChoiceList9 = ['Полностью согласен'] * 36 + ['Согласен'] * 21 + ['Не уверен'] * 21 + ['Не согласен'] * 12 + ['Категорически не согласен'] * 10
ChoiceList10 = ['Полностью согласен'] * 29 + ['Согласен'] * 25 + ['Не уверен'] * 25 + ['Не согласен'] * 12 + ['Категорически не согласен'] * 9
ChoiceList11 = ['Полностью согласен'] * 23 + ['Согласен'] * 41 + ['Не уверен'] * 11 + ['Не согласен'] * 16 + ['Категорически не согласен'] * 9
ChoiceList12 = ['Полностью согласен'] * 26 + ['Согласен'] * 37 + ['Не уверен'] * 11 + ['Не согласен'] * 12 + ['Категорически не согласен'] * 14
ChoiceList13 = ['Полностью согласен'] * 18 + ['Согласен'] * 23 + ['Не уверен'] * 29 + ['Не согласен'] * 16 + ['Категорически не согласен'] * 14
ChoiceList14 = ['Полностью согласен'] * 24 + ['Согласен'] * 16 + ['Не уверен'] * 30 + ['Не согласен'] * 14 + ['Категорически не согласен'] * 16
ChoiceList15 = ['Полностью согласен'] * 21 + ['Согласен'] * 23 + ['Не уверен'] * 27 + ['Не согласен'] * 11 + ['Категорически не согласен'] * 18
ChoiceList16 = ['Полностью согласен'] * 32 + ['Согласен'] * 18 + ['Не уверен'] * 23 + ['Не согласен'] * 16 + ['Категорически не согласен'] * 11
ChoiceList17 = ['Полностью согласен'] * 20 + ['Согласен'] * 18 + ['Не уверен'] * 32 + ['Не согласен'] * 14 + ['Категорически не согласен'] * 16
ChoiceList18 = ['Полностью согласен'] * 16 + ['Согласен'] * 32 + ['Не уверен'] * 27 + ['Не согласен'] * 14 + ['Категорически не согласен'] * 11
ChoiceList19 = ['Полностью согласен'] * 18 + ['Согласен'] * 30 + ['Не уверен'] * 20 + ['Не согласен'] * 18 + ['Категорически не согласен'] * 14
ChoiceList20 = ['Полностью согласен'] * 20 + ['Согласен'] * 40 + ['Не уверен'] * 18 + ['Не согласен'] * 12 + ['Категорически не согласен'] * 10
ChoiceList21 = ['Полностью согласен'] * 10 + ['Согласен'] * 44 + ['Не уверен'] * 20 + ['Не согласен'] * 10 + ['Категорически не согласен'] * 16


for i in range(400):
    gender = GenderList[random.randint(0, 99)]
    age = AgeList[random.randint(0, 99)]
    edu = EduList[random.randint(0, 99)]
    work = WorkList[random.randint(0, 99)]
    inc = IncomeList[random.randint(0, 99)]
    freq = FreqList[random.randint(0, 99)]
    und = UndList[random.randint(0, 99)]
    agg = AggList[random.randint(0, 99)]
    ImpList = ['Производитель', 'Мое знание о лекарстве', 'Прошлый опыт использования',
               'Наличие в запасе (лекарство доступно для покупки в любой момент времени)',
               'Наличие в разных местах (лекарство можно купить в большом количестве мест)', 'Цена',
               'Мнение близких людей', 'Мнение специалистов (врачи/аптекари и т.п.)',
               'Общественное мнение и мнение инфлюенсеров (знаменитости, блогеры)', 'Реклама лекарства',
               'Дизайн упаковки']

    imp = ImpList.pop(random.randint(0, 10))
    imp1 = ImpList.pop(random.randint(0, 9))
    imp2 = ImpList.pop(random.randint(0, 8))
    # imp3 = ImpList.pop(random.randint(0, 7))
    form_data = {
        'entry.470600391': gender,
        'entry.880153186': age,
        'entry.1453013777': edu,
        'entry.512265841': work,
        'entry.1842944679': inc,
        'entry.707600964': freq,
        'entry.759575254': und,
        'entry.1052322623': agg,
        'entry.1560053697': [imp, imp1, imp2],
        'entry.1845154714': ChoiceList1[random.randint(0, 99)],
        'entry.1590148524': ChoiceList2[random.randint(0, 99)],
        'entry.1576509728': ChoiceList3[random.randint(0, 99)],
        'entry.1500951550': ChoiceList4[random.randint(0, 99)],
        'entry.1587219546': ChoiceList5[random.randint(0, 99)],
        'entry.68566109': ChoiceList6[random.randint(0, 99)],
        'entry.955951090': ChoiceList7[random.randint(0, 99)],
        'entry.1064880090': ChoiceList8[random.randint(0, 99)],
        'entry.2121621143': ChoiceList9[random.randint(0, 99)],
        'entry.1986223385': ChoiceList10[random.randint(0, 99)],
        'entry.1574801775': ChoiceList11[random.randint(0, 99)],
        'entry.934227220': ChoiceList12[random.randint(0, 99)],
        'entry.559337149': ChoiceList13[random.randint(0, 99)],
        'entry.1868271741': ChoiceList14[random.randint(0, 99)],
        'entry.1584804972': ChoiceList15[random.randint(0, 99)],
        'entry.987814094': ChoiceList16[random.randint(0, 99)],
        'entry.2009468143': ChoiceList17[random.randint(0, 99)],
        'entry.1633842567': ChoiceList18[random.randint(0, 99)],
        'entry.670972188': ChoiceList19[random.randint(0, 99)],
        'entry.838221325': ChoiceList20[random.randint(0, 99)],
        'entry.1048212391': ChoiceList21[random.randint(0, 99)],
    }
    user_agent = {'Referer':urlReferer,'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    r = requests.post(urlResponse, data=form_data, headers=user_agent)
    if r == '400':
        print(form_data)
    print(i, r)
