import sys

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets

from res.ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

        self.image = None
        self.timer_camera = QtCore.QTimer()
        self.cam = cv2.VideoCapture()
        self.CAM_NUM = 0

        self.init_slot()

    def init_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def init_slot(self):
        self.timer_camera.timeout.connect(self.camera_start_preview)
        self.ui.btn_cam_open.clicked.connect(self.clicked_camera_open)
        self.ui.btn_cam_close.clicked.connect(self.clicked_camera_close)

    def camera_start_preview(self):
        flag, self.image = self.cam.read()
        show = cv2.resize(self.image, (440, 330))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        show_image = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.ui.label_cam_preview.setPixmap(QtGui.QPixmap.fromImage(show_image))

    def clicked_camera_open(self):
        if not self.timer_camera.isActive():
            flag = self.open_camera(True)
            if not flag:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"Please make sure if camera is plugged in.",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                print('+++start preview+++')
                self.timer_camera.start(30)
        else:
            self.clicked_camera_close()

    def clicked_camera_close(self):
        if self.timer_camera.isActive():
            print('---stop preview---')
            self.timer_camera.stop()
        self.open_camera(False)

        self.ui.label_cam_preview.clear()

    def closeEvent(self, event):
        self.clicked_camera_close()
        # ok = QtWidgets.QPushButton()
        # cacel = QtWidgets.QPushButton()
        #
        # msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"Close", u"Close!")
        #
        # msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        # msg.addButton(cancel, QtWidgets.QMessageBox.RejectRole)
        # ok.setText(u'OK')
        # cacel.setText(u'Cancel')
        # if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
        #     event.ignore()
        # else:
        #     if self.cap.isOpened():
        #         self.cap.release()
        #     if self.timer_camera.isActive():
        #         self.timer_camera.stop()
        #     event.accept()

    def open_camera(self, b):
        self.set_button_enable(not b)
        flag = True
        if b:
            if not self.cam.isOpened():
                print('+++open cam+++')
                flag = self.cam.open(self.CAM_NUM)
                print('---open cam---')
            else:
                print('cam is already opened')
        else:
            if self.cam.isOpened():
                print('+++close cam+++')
                self.cam.release()
                print('---close cam---')
            else:
                print('cam is already closed')

        return flag

    def set_button_enable(self, b):
        self.ui.btn_cam_open.setEnabled(b)
        self.ui.btn_cam_close.setEnabled(not b)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
