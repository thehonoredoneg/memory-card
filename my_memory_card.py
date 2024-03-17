from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGroupBox, QPushButton,
    QRadioButton, QLabel, QVBoxLayout, QHBoxLayout,
    QButtonGroup, QMessageBox
)
import random


class Question:
    def __init__(self, text, right_answer, wrong1, wrong2, wrong3):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions = [
    Question('Какая планета находится ближе всего к Солнцу?', 'Венера', 'Марс', 'Земля', 'Юпитер'),
    Question('Кто написал произведение "Война и мир"?', 'Лев Толстой', 'Федор Достоевский', 'Александр Пушкин', 'Иван Тургенев'),
    Question('В каком году была подписана Декларация независимости США?', '1776', '1789', '1801', '1865'),
    Question('Какой химический элемент имеет символ "H" в периодической таблице?', 'Гидроген', 'Гелий', 'Гафний', 'Германий'),
    Question('Какой океан является самым большим по площади?', 'Тихий океан', 'Атлантический океан', 'Индийский океан', 'Северный Ледовитый океан'),
    Question('Какая страна является родиной футбола (футбольного футбола)?', 'Бразилия', 'Италия', 'Англия', 'Аргентина'),
    Question('Какое животное является символом Австралии?', 'Кенгуру', 'Коала', 'Эму', 'Дельфин'),
    Question('Какой газ составляет большую часть атмосферы Земли?', 'Азот', 'Кислород', 'Углекислый газ', 'Аргон')
]


def is_checked():
    for rbtn in answers_btn:
        if rbtn.isChecked():
            return True
    return False


def show_result():
    if not is_checked():
        return
    
    btn.setText('Следующий вопрос')  
    for rbtn in answers_btn:  
        rbtn.setDisabled(True)
        if rbtn.isChecked():  
            if rbtn.text() == answers_btn[0].text(): 
                rbtn.setStyleSheet('color: green;')
                main_win.score += 1  
            else:
                rbtn.setStyleSheet('color: red;')  
                answers_btn[0].setStyleSheet('color: green;') 
            break
        


def show_question():
    next_question()
    btn.setText('Ответить')  
    button_group.setExclusive(False)  
    for rbtn in answers_btn: 
        rbtn.setDisabled(False)
        rbtn.setChecked(False)  
        rbtn.setStyleSheet('')  
    button_group.setExclusive(True)  


def start_test():
    if btn.text() == 'Ответить':  
        show_result()  
    else:  
        show_question() 


def ask(q: Question):
    question_text.setText(q.text)  
    random.shuffle(answers_btn) 
    answers_btn[0].setText(q.right_answer)  
    answers_btn[1].setText(q.wrong1)  
    answers_btn[2].setText(q.wrong2)  
    answers_btn[3].setText(q.wrong3)  


def next_question():
    if main_win.q_index == len(questions) - 1:
        main_win.q_index = -1
        random.shuffle(questions)
        show_score()
        main_win.score = 0

    main_win.q_index += 1
    q = questions[main_win.q_index]
    ask(q)

def show_score():
    percent = main_win.score / main_win.total * 100
    percent = round(percent, 2)
    text = 'Уважаемый пользователь!\n'
    text += 'Вы ответили правильно на ' + str(main_win.score) + ' из ' + str(main_win.total) + ' вопросов.\n'
    text += 'Процент правильных ответов равен ' + str(percent) + '%'

    msg = QMessageBox()
    msg.setWindowTitle('')
    msg.setText(text)
    msg.exec()

app = QApplication([])  
main_win = QWidget()  
main_win.setWindowTitle('MemoryCard')  
main_win.resize(640, 480)  
main_win.q_index = -1
main_win.score = 0 
main_win.total = len(questions) 

question_text = QLabel('Тут будет вопрос?') 
grp_box = QGroupBox('Варианты ответов')  
radio1 = QRadioButton('Нет')  
radio2 = QRadioButton('Да') 
radio3 = QRadioButton('Что') 
radio4 = QRadioButton('Зачем?') 
btn = QPushButton('Ответить')  



answers_btn = [radio1, radio2, radio3, radio4]



button_group = QButtonGroup()
button_group.addButton(radio1)
button_group.addButton(radio2)
button_group.addButton(radio3)
button_group.addButton(radio4)


main_layout = QVBoxLayout()  
main_h1 = QHBoxLayout()  
main_h2 = QHBoxLayout()  
main_h3 = QHBoxLayout()  
grp_layout = QHBoxLayout()  
grp_v1 = QVBoxLayout()  
grp_v2 = QVBoxLayout()  



main_h1.addWidget(question_text, alignment=Qt.AlignCenter)  
main_h2.addWidget(grp_box)  
main_h3.addStretch(1)
main_h3.addWidget(btn, stretch=3)
main_h3.addStretch(1)
main_layout.addLayout(main_h1)
main_layout.addLayout(main_h2)
main_layout.addLayout(main_h3)
grp_v1.addWidget(radio1)
grp_v1.addWidget(radio2)
grp_v2.addWidget(radio3)
grp_v2.addWidget(radio4)
grp_layout.addLayout(grp_v1)
grp_layout.addLayout(grp_v2)
grp_box.setLayout(grp_layout)
main_win.setLayout(main_layout)


btn.clicked.connect(start_test)  

random.shuffle(questions)  
next_question()

main_win.show()
app.exec()