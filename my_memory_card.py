from PyQt5 import Qt
from PyQt5.QtWidgets import QButtonGroup, QApplication, QWidget, QBoxLayout, QHBoxLayout,QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel
from random import shuffle, randint
#создай приложение для запоминания информации
class Question():
    def __init__(self, question, rigt_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.rigt_answer = rigt_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(500, 400)

que_list = []
que_list.append(Question("Государственный язык Бразилии", "Португальский", "Англиский", "Испанский", "Бразильский"))
que_list.append(Question("Какой национальности не существует?","Смурфы","Энцы", "Чульмцы","Алеуты"))
que_list.append(Question("В каком году произошло бородинское сражение?","1812","1820", "1703","1942"))
que_list.append(Question("В каком году первый человек отправился в космос?","1961","1960", "2005","1938"))
que_list.append(Question("В какой стране больше всего языков?","Новая Гвинея","Куба", "Япония","Китай"))
que_list.append(Question("В каком году был создан язык программировании Python","1991","1986", "2001","1994"))
que_list.append(Question("Какая есть пишится Пайтон? (На англ.)","Python","Pyhton", "Pascal","Пайтон"))
que_list.append(Question("Сколько месяцев в году?","12","13", "9","3"))
que_list.append(Question("Сколько в одном квартале месяцев?","3","12", "6", "1"))
que_list.append(Question("Сколько битов в байте?","8","64", "1024","24"))




btn_Ok = QPushButton("Ответить")
lb_Question=QLabel("Какой национальности не существует?")
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чульмцы")
rbtn_4 = QRadioButton("Алеуты")
layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()

layout_2.addWidget(rbtn_1)
layout_2.addWidget(rbtn_2)
layout_3.addWidget(rbtn_3)
layout_3.addWidget(rbtn_4)
layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)

RadioGroupBox.setLayout(layout_1)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_Ok, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)
main_win.setLayout(layout_card)

AnsGB = QGroupBox("Результаты теста")
lb_result = QLabel("Прав ты или нет?")
lb_correct = QLabel("Ответ будет тут!")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_correct, stretch=2)
AnsGB.setLayout(layout_res)
layout_line2.addWidget(AnsGB)
AnsGB.hide()

radioG = QButtonGroup()
radioG.addButton(rbtn_1)
radioG.addButton(rbtn_2)
radioG.addButton(rbtn_3)
radioG.addButton(rbtn_4)
def show_result():
    RadioGroupBox.hide()
    AnsGB.show()
    btn_Ok.setText("Следующий вопрос")
def show_qeu():
    RadioGroupBox.show()
    AnsGB.hide()
    btn_Ok.setText("Ответить")
    radioG.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radioG.setExclusive(True)


answers = [ rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.rigt_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_correct.setText(q.rigt_answer)
    show_qeu()
def show_corret(res):
    lb_result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_corret("Правельно")
        main_win.score += 1
        print("Всего вопросов:", main_win.total, "\n-Правельных ответов:", main_win.score)
        print("Рейтинг:", ((main_win.score/main_win.total) * 100), " %" )
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_corret("Неверно")
            print("Рейтинг:", ((main_win.score/main_win.total) * 100), " %" )
def  next_que():
    main_win.total += 1
    print("Рейтинг:", ((main_win.score/main_win.total) * 100), " %" )
    """main_win.cur_que = main_win.cur_que + 1"""
    cur_que = randint(0, len(que_list)-1)
    q = que_list[cur_que]
    """if main_win.cur_que >=len(que_list):
        main_win.cur_que = 0
    q = que_list[main_win.cur_que]"""
    ask(q)
def click_OK():
    if btn_Ok.text()== "Ответить":
        check_answer()
    else:
        next_que()


main_win.cur_que = -1
btn_Ok.clicked.connect(click_OK)
main_win.score = 0
main_win.total = 0
next_que()
main_win.show()
app.exec_()


