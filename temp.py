#from PyQt5.QtCore import Q
from PyQt5.QtWidgets import QWidget, QLabel, QListWidget, QTreeWidget, QHBoxLayout, QVBoxLayout, QGridLayout
import json, hashlib

data = None

def read():
    global data
    with open("users.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
    print(data)

def write():
    global data
    with open("users.json", "w+", encoding="utf-8") as file:
        json.dump(data, file, sort_keys=True, indent=4, ensure_ascii=False)
        print(hashlib.md5(data).hexdigest())

    print(data)

read()
data["Артемий"] = {"timetable": "",
                   "homework": "",
                   "picture": "",
                   "mail": ""}
write()