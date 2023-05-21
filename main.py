from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QTextEdit, QListWidget


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Программа контроля обучения учеников')
main_win.resize(1280,720)

lbl_schedule = QLabel("Расписание")
lbl_schedule_today = QLabel("Расписание на сегодня")
button = QPushButton('Изменить данные ученика')
btn_add_student = QPushButton('Добавить ученика')
btn_send_homework = QPushButton('Отправить')
btn_change_schedule = QPushButton('Изменить расписание')
text_homework= QTextEdit()
text_homework.setPlaceholderText("Введите текст ДЗ")
list_schedule = QListWidget()
list_students = QListWidget()
list_schedule_today = QListWidget()

# main_win.setLayout(v_line)
main_win.show()
app.exec_()
