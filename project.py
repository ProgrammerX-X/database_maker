# ======================
#                       ||
# Coder: Tkalich Alina ||
#                       ||
# =====================

import sys
from PyQt6.QtWidgets import QPushButton, QMainWindow, QLabel, QApplication, QRadioButton, QButtonGroup, QFileDialog, QCheckBox,\
    QTextEdit
from PyQt6.QtGui import QFont
import os
from faker_data import faker_function
from selector import select

from saver import getter

class queryWindow(QMainWindow):
    def __init__(self, database):
        super().__init__()
        self.setWindowTitle("Queries...")
        self.resize(600, 400)
        self.move(350, 160)

        self.queries = QTextEdit(self)
        self.queries.setPlaceholderText("Terminal for MySql database...\n")
        self.queries.move(20, 20)
        self.queries.setFixedSize(550, 300)
        self.queries.setFont(QFont("Arial", 12))

        self.submit = QPushButton("Submit", self)
        self.submit.setFixedSize(120, 40)
        self.submit.setFont(QFont("Arial", 10))
        self.submit.move(450, 350)

        self.response = ""

        self.submit.clicked.connect(lambda: self.e_o_n(database))
        self.q = self.get_text()

        self.label = QLabel("Terminal", self)
        self.label.setWordWrap(True)
        self.label.setFixedSize(420, 100)
        self.label.setFont(QFont("Arial", 10))
        self.label.move(20, 305)

        self.show()
    def e_o_n(self, db):
        self.datas = self.get_text()
        self.response = getter(db, self.datas)
        self.label.setText(str(self.response))
    def get_text(self):
        self.q = self.queries.toPlainText()
        return self.q


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Making Database")
        self.resize(600, 400)
        self.move(350, 160)

        self.label = QLabel("Database Maker", self)
        label_font = QFont("Arial", 20)
        self.label.move(215, 10)
        self.label.setFixedSize(600, 50)
        self.label.setFont(label_font)

        self.check_making = QLabel("Making Database", self)
        check_font = QFont("Arial", 12)
        self.check_making.setFont(check_font)
        self.check_making.move(60, 80)
        self.check_making.setFixedSize(130, 20)

        self.check_update = QLabel("Update Database", self)
        self.check_update.setFont(check_font)
        self.check_update.move(390, 80)
        self.check_update.setFixedSize(130, 20)

        self.check_faker = QRadioButton("Faker data", self)
        radio_font = QFont("Arial", 10)
        self.check_faker.move(60, 120)
        self.check_faker.setFont(radio_font)
        self.check_faker.setFixedSize(130, 20)

        self.clicker = 0
        self.check_faker.clicked.connect(self.f_f)

        self.check_own_file = QRadioButton("Select my own file", self)
        self.check_own_file.move(60, 150)
        self.check_own_file.setFont(radio_font)
        self.check_own_file.setFixedSize(130, 20)

        self.own_file = QPushButton("Select file...", self)
        self.own_file.move(60, 180)
        self.own_file.setFont(radio_font)
        self.own_file.setFixedSize(130, 20)
        self.own_file.setVisible(False)
        self.database = ""
        self.own_file.clicked.connect(lambda: self.open_files("Database files (*.db)", 1))

        self.check_own_file.clicked.connect(lambda: self.own_file.setVisible(True))
        
        self.checking_db = QButtonGroup(self)
        self.checking_db.addButton(self.check_faker)
        self.checking_db.addButton(self.check_own_file)

        self.selected = QLabel("NaN...", self)
        self.selected.move(390, 120)
        self.selected.setFont(radio_font)
        self.selected.setFixedSize(130, 20)
        
        self.query = QPushButton("Write query", self)
        self.query.setFixedSize(130, 20)
        self.query.move(390, 150)
        self.query.setFont(radio_font)
        self.query.setVisible(False)

        self.query.clicked.connect(self.new_window_query)

        self.file_w_q = QPushButton("File with queries", self)
        self.file_w_q.setVisible(False)
        self.file_w_q.setFixedSize(130, 20)
        self.file_w_q.setFont(radio_font)
        self.file_w_q.move(390, 180)
        self.csv_file = ""
        self.file_w_q.clicked.connect(lambda: self.open_files("CSV files (*.csv)", 2))
        self.file_w_q.clicked.connect(self.save_err)
        self.error_or_not = ""
        

        self.label_about_correct = QLabel("", self)
        self.label_about_correct.setWordWrap(True)
        self.label_about_correct.setFixedSize(100, 200)
        self.label_about_correct.setFont(radio_font)
        self.label_about_correct.move(400, 200)
        self.show()
    
    def save_err(self):
        self.error_or_not = select(self.database, self.csv_file)
        self.label_about_correct.setText(self.error_or_not)

    def f_f(self):
        if self.clicker == 0:
            name = faker_function()
            self.selected.setText(name)
            self.query.setVisible(True)
            self.file_w_q.setVisible(True)
            self.own_file.setVisible(False)
            self.database = name
            print(name)
            self.clicker+=1
        else:
            self.own_file.setVisible(False)
    
    def open_files(self, filter, par):
        if par == 1:
            filepath, _ = QFileDialog.getOpenFileName(self, "Open file...", "..\\Ex6\\DbData", filter)
            db = os.path.basename(filepath)
            if db:
                self.selected.setText(db)
                self.query.setVisible(True)
                self.file_w_q.setVisible(True)
                self.database = db
        elif par == 2:
            filepath, _ = QFileDialog.getOpenFileName(self, "Open file...", "..\\Ex6\\DbData", filter)
            csv = os.path.basename(filepath)
            if csv:
                self.csv_file = csv

    def new_window_query(self):
        self.queries = queryWindow(self.database)
        self.queries.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
