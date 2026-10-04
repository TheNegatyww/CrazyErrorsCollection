import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl
from PySide6.QtGui import QKeyEvent


VIDEO = "film11.mp4"


class VideoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showFullScreen()

        self.video = QVideoWidget()
        self.setCentralWidget(self.video)

        self.player = QMediaPlayer()
        self.audio = QAudioOutput()

        self.player.setVideoOutput(self.video)
        self.player.setAudioOutput(self.audio)

        self.audio.setVolume(1.0)

        self.player.setSource(QUrl.fromLocalFile(VIDEO))
        self.player.play()

        self.player.mediaStatusChanged.connect(self.video_finished)

    def video_finished(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.close()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == 16777216:  # ESC
            self.player.stop()
            self.close()


app = QApplication(sys.argv)

window = VideoWindow()
window.show()

sys.exit(app.exec())
