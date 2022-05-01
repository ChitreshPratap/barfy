import sys
import time

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget

from barfi.chitrapat.SplashConfig import SplashConfig
from barfi.chitrapat.SplashScreen_Dark import SplashScreen_Dark

class SplashScreen_DarkEx(SplashScreen_Dark):
    
    def __init__(self,app=None,timeoutSeconds:int=10,splashConfig:SplashConfig=None):
        super(SplashScreen_DarkEx, self).__init__()

        if splashConfig is None:
            splashConfig=SplashConfig()
            splashConfig.setAppTitle("App Title").setAppTagLine("Application Tag Line").setCompanyName("Company Name")
        title=splashConfig.getAppTitle()
        titleDesc=splashConfig.getAppTagLine()
        appIconPath=splashConfig.getAppIcon()

        self.label_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">{appName}</span></p></body></html>".format(appName=title))
        self.label_3.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline; color:#bfbfbf;\">{appTagLine}</span></p></body></html>".format(appTagLine=titleDesc))
        appIconPixMap=QtGui.QPixmap(appIconPath)
        self.label.setPixmap(appIconPixMap)
        self._app=app
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        s="""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
            }
            
            QProgressBar::chunk {
                background-color: rgb(235, 123, 49);
                width: 20px;
            }
        """
        self.progressBar.setStyleSheet(s)
        self.progressBar.setMaximum(10)
        qr=self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.show()

        # self.showMessage("<h1><font color='green'>Welcome BeeMan!</font></h1>", Qt.AlignTop | Qt.AlignCenter,
        #                  Qt.black)
        for i in range(1, 11):
            self.progressBar.setValue(i)
            t = time.time()
            while time.time() < t + 0.1:
                if self._app is not None:
                    self._app.processEvents()

        # Simulate something that takes time
        time.sleep(timeoutSeconds)

    def finish(self,mainWindow):
        super(SplashScreen_DarkEx, self).finish(mainWindow)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dlg=SplashScreen_DarkEx(app,5)
    dlg.show()
    app.exec()

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QSplashScreen
# from src.styles import appResources
#
# class SplashScreen_Dark(QSplashScreen):
#
#     def __init__(self):
#         super(SplashScreen_Dark, self).__init__()
#         self.setupUi()
#
#     def setupUi(self):
#         Dialog = self