from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout  # importing QLabel to be the basis of our labels
from PyQt5.QtCore import Qt  # importing Qt for alignment abilities
from PyQt5.QtGui import QPixmap


# creating a default large test label to be reused wherever needed
def large_text_label(text):  # takes argument of text for easy customisation
    label = QLabel(text)  # our label will be an object of the pre-configured class QLabel
    label.setAlignment(Qt.AlignCenter)  # setting text alignment so label contents are always centered
    label.setStyleSheet("""
                font-helvetica;
                font-size: 40px;
                color: black;
                """)  # using style sheet to set visual properties
    return label  # returning our label to the caller


class Image(QWidget):
    def __init__(self, display_image):
        super().__init__()
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        display_image = display_image

        image = QLabel()

        pixmap = QPixmap(display_image)
        scaled_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        image.setPixmap(scaled_pixmap)

        image.setScaledContents(True)
        image.setFixedSize(scaled_pixmap.size())

        self.main_layout.addWidget(image)