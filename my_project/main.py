from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5 import uic

class CalculatorApp(QDialog):
    def __init__(self):
        super().__init__()

        # Завантажуємо UI з файлу .ui
        uic.loadUi("my_app.ui", self)

        # Налаштування стилю
        self.setStyleSheet("""
            QPushButton {
                background-color: rgb(205, 217, 255);
                color: black;
                border-radius: 0px;
                font-size: 20px;
            }
            QPushButton#pushButton_c {
                background-color: rgb(205, 217, 255);
                color: red;
            }
        """)

        # Підключення функцій до кнопок
        self.pushButton_0.clicked.connect(lambda: self.add_digit("0"))
        self.pushButton_1.clicked.connect(lambda: self.add_digit("1"))
        self.pushButton_2.clicked.connect(lambda: self.add_digit("2"))
        self.pushButton_3.clicked.connect(lambda: self.add_digit("3"))
        self.pushButton_4.clicked.connect(lambda: self.add_digit("4"))
        self.pushButton_5.clicked.connect(lambda: self.add_digit("5"))
        self.pushButton_6.clicked.connect(lambda: self.add_digit("6"))
        self.pushButton_7.clicked.connect(lambda: self.add_digit("7"))
        self.pushButton_8.clicked.connect(lambda: self.add_digit("8"))
        self.pushButton_9.clicked.connect(lambda: self.add_digit("9"))
        self.pushButton_plus.clicked.connect(lambda: self.add_operator("+"))
        self.pushButton_minus.clicked.connect(lambda: self.add_operator("-"))
        self.pushButton_x.clicked.connect(lambda: self.add_operator("×"))
        self.pushButton_dilen.clicked.connect(lambda: self.add_operator("÷"))
        self.pushButton_summa.clicked.connect(self.calculate)
        self.pushButton_c.clicked.connect(self.clear_label)

        self.current_input = ""
        self.operator = None
        self.first_operand = None

    def add_digit(self, digit):
        self.current_input += digit
        self.label_Output.setText(self.current_input)

    def add_operator(self, operator):
        if self.current_input:
            if self.first_operand is None:
                self.first_operand = float(self.current_input)
            self.operator = operator
            self.current_input = ""
            self.label_Output.setText(operator)

    def calculate(self):
        if self.first_operand is not None and self.operator and self.current_input:
            second_operand = float(self.current_input)
            if self.operator == "+":
                result = self.first_operand + second_operand
            elif self.operator == "-":
                result = self.first_operand - second_operand
            elif self.operator == "×":
                result = self.first_operand * second_operand
            elif self.operator == "÷":
                if second_operand == 0:
                    result = "Error"
                else:
                    result = self.first_operand / second_operand
            self.label_Output.setText(str(result))
            self.first_operand = result
            self.operator = None
            self.current_input = ""

    def clear_label(self):
        self.current_input = ""
        self.first_operand = None
        self.operator = None
        self.label_Output.setText("")

app = QApplication([])
window = CalculatorApp()
window.show()
app.exec_()