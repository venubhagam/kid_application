import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QStackedWidget, QFrame
)
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtGui import QFont, QPixmap


# -------- CONTENT PAGE -------- #
class ContentPage(QWidget):
    def __init__(self, title, text, image_path):
        super().__init__()

        layout = QVBoxLayout()

        self.title = QLabel(title)
        self.title.setFont(QFont("Arial", 20, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)

        self.image = QLabel()
        pixmap = QPixmap(image_path)
        self.image.setPixmap(pixmap.scaled(250, 250, Qt.KeepAspectRatio))
        self.image.setAlignment(Qt.AlignCenter)

        self.text = QLabel(text)
        self.text.setWordWrap(True)
        self.text.setFont(QFont("Arial", 12))
        self.text.setAlignment(Qt.AlignTop)

        layout.addWidget(self.title)
        layout.addWidget(self.image)
        layout.addWidget(self.text)

        self.setLayout(layout)


# -------- MAIN WINDOW -------- #
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Computer Basics Learning")
        self.setGeometry(100, 100, 900, 500)

        main_layout = QHBoxLayout()

        # -------- LEFT PANEL (MENU) -------- #
        self.menu = QVBoxLayout()

        self.buttons = []

        topics = [
            "What is a Computer",
            "Keyboard & Mouse",
            "Files & Folders",
            "Operating System",
            "Text Editors",
            "Internet Safety",
            "Problem Solving",
            "Numbers & Logic"
        ]

        for i, topic in enumerate(topics):
            btn = QPushButton(topic)
            btn.setStyleSheet("""
                QPushButton {
                    padding: 10px;
                    font-size: 14px;
                    background-color: #3498db;
                    color: white;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)
            btn.clicked.connect(lambda checked, i=i: self.display_page(i))
            self.menu.addWidget(btn)
            self.buttons.append(btn)

        menu_frame = QFrame()
        menu_frame.setLayout(self.menu)
        menu_frame.setFixedWidth(220)

        # -------- RIGHT PANEL (CONTENT) -------- #
        self.stack = QStackedWidget()

        self.pages = [
            ContentPage("What is a Computer",
                        "A computer is an electronic device that processes data.",
                        "images/computer.png"),

            ContentPage("Keyboard & Mouse",
                        "Keyboard is used to type. Mouse is used to click.",
                        "images/keyboard.png"),

            ContentPage("Files & Folders",
                        "Files store data. Folders organize files.",
                        "images/folder.png"),

            ContentPage("Operating System",
                        "OS manages the computer like Windows, Linux.",
                        "images/os.png"),

            ContentPage("Text Editors",
                        "Used to write text like Notepad.",
                        "images/text.png"),

            ContentPage("Internet Safety",
                        "Do not share personal info online.",
                        "images/internet.png"),

            ContentPage("Problem Solving",
                        "Break problems into small steps.",
                        "images/problem.png"),

            ContentPage("Numbers & Logic",
                        "Basic math and thinking skills.",
                        "images/numbers.png"),
        ]

        for page in self.pages:
            self.stack.addWidget(page)

        main_layout.addWidget(menu_frame)
        main_layout.addWidget(self.stack)

        self.setLayout(main_layout)

    # -------- PAGE SWITCH WITH ANIMATION -------- #
    def display_page(self, index):
        self.stack.setCurrentIndex(index)

        # Fade animation
        self.anim = QPropertyAnimation(self.stack.currentWidget(), b"windowOpacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.start()


# -------- RUN APP -------- #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())