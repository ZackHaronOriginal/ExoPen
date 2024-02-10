from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from screeninfo import get_monitors
from pynput import mouse
import sys
import draw_window


class Main(QWidget):
    def __init__(self):
        super().__init__()

        #region Variables

        #region TODO[epic=Variables] ScreenSizeInfo

        screen_size = []

        for m in get_monitors():
            screen_size.append(m.width)
            screen_size.append(m.height)

        x_width = 50
        x_pos = screen_size[0] - x_width
        y_pos = 0

        self.move(x_pos, y_pos)
        #endregion

        #region TODO[epic=Variables] Element Control Variables

        self.main_window_icon_size = 40
        self.main_window_icon_height_offsett = 10

        self.move_labe_margin_size = 5
        
        self.button_background_color_name = "white;"
        self.button_background_color = "background-color : white;"
        
        self.button_border_color_name = "darkCyan"
        self.button_border_type =  "border :3px solid;"
        self.button_border_color_up = "border-top-color : {};".format(self.button_border_color_name)
        self.button_border_color_down = "border-bottom-color : {};".format(self.button_border_color_name)
        self.button_border_color_right = "border-right-color : {};".format(self.button_border_color_name)
        self.button_border_color_left = "border-left-color : {};".format(self.button_border_color_name)
        self.button_border_curves = """      
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 10px;"""

        #endregion

        #region TODO[epic=Variables] Data Holders

        self.oldPos = self.pos()

        #endregion

        #endregion
        
        #region Creating Layout

        #region TODO[epic=LayoutCreation] Creating Elements

        #region TODO[epic=LayoutCreation] Main Window

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.move_label = QLabel("" , self)
        self.button_mouse = QPushButton("", self)
        self.button_pen = QPushButton("", self)
        self.button_line = QPushButton("", self)
        self.button_shape = QPushButton("", self)
        self.button_whiteboard = QPushButton("", self)
        self.button_eraser = QPushButton("", self)
        self.button_clear = QPushButton("", self)
        self.button_settings = QPushButton("", self)
        self.button_color = QPushButton("", self)

        #endregion

        #region TODO[epic=LayoutCreation] Tray

        self.tray = QSystemTrayIcon()
        self.tray_menu = QMenu()
        self.tray_menu_show = QAction("Show")
        self.tray_menu_minimize = QAction("Minimize")
        self.tray_menu_exit = QAction("Quit")

        #endregion

        #region TODO[epic=LayoutCreation] Sub Window

        self.sub_window = draw_window.DrawWindow()

        #endregion


        #region TODO[epic=LayoutCreation] Adding Into The Layouts

        #region Main Window Layout

        self.layout.addWidget(self.move_label)
        self.layout.addWidget(self.button_mouse)
        self.layout.addWidget(self.button_pen)
        self.layout.addWidget(self.button_line)
        self.layout.addWidget(self.button_shape)
        self.layout.addWidget(self.button_whiteboard)
        self.layout.addWidget(self.button_eraser)
        self.layout.addWidget(self.button_clear)
        self.layout.addWidget(self.button_settings)
        self.layout.addWidget(self.button_color)

        #endregion

        #region Main Window Buttons

        self.button_mouse.clicked.connect(self.OnButtonMouseClick)
        self.button_pen.clicked.connect(self.OnButtonPenClick)
        self.button_line.clicked.connect(self.OnButtonLineClick)
        self.button_shape.clicked.connect(self.OnButtonShapeClick)
        self.button_whiteboard.clicked.connect(self.OnButtonWhiteboardClick)
        self.button_eraser.clicked.connect(self.OnButtonEraserClick)
        self.button_clear.clicked.connect(self.OnButtonClearClick)
        self.button_settings.clicked.connect(self.OnButtonSettingsClick)
        self.button_color.clicked.connect(self.OnButtonColorClick)

        #endregion

        #region Sub Window Elements

        self.sub_window.mouse_clicked.connect(self.OnSubWindowClicked)

        #endregion

        #region Tray Layout

        self.tray_menu.addAction(self.tray_menu_show)
        self.tray_menu.addAction(self.tray_menu_minimize)
        self.tray_menu.addAction(self.tray_menu_exit)

        #endregion
        
        #endregion


        #region TODO[epic=LayoutCreation] Setting The Elements Properties

        #region Main Window Properties

        self.move_label_pixmap = QPixmap("Images/Exo_Pen_Logo_Icon.png")
        self.move_label_pixmap = self.move_label_pixmap.scaled(self.main_window_icon_size, self.main_window_icon_size + self.main_window_icon_height_offsett, Qt.KeepAspectRatio)
        self.move_label.setPixmap(self.move_label_pixmap)
        self.move_label.setAlignment(Qt.AlignCenter)
        self.move_label.setMargin(self.move_labe_margin_size)

        self.button_mouse.setIcon(QIcon("Images/Exo_Pen_Mouse_Logo.png"))
        self.button_mouse.setStyleSheet(
        f"""

        {self.button_background_color}
        {self.button_border_type}
        {self.button_border_color_up}
        border-bottom-color : {self.button_background_color_name}
        {self.button_border_color_right}
        {self.button_border_color_left}
        {self.button_border_curves}
        

        """)
        self.button_mouse.setIconSize(QSize(self.main_window_icon_size, self.main_window_icon_size + self.main_window_icon_height_offsett))

        self.button_pen.setIcon(QIcon("Images/Exo_Pen_Logo_Version0.png"))
        self.button_pen.setStyleSheet(
        f"""

        {self.button_background_color}
        {self.button_border_type}
        border-top-color : {self.button_background_color_name}
        border-bottom-color : {self.button_background_color_name}
        {self.button_border_color_right}
        {self.button_border_color_left}
        {self.button_border_curves}

        """)
        self.button_pen.setIconSize(QSize(self.main_window_icon_size, self.main_window_icon_size + self.main_window_icon_height_offsett))

        self.button_line.setIcon(QIcon("Images/Exo_Pen_Lines_Large.png"))
        self.button_line.setStyleSheet(
        f"""

        {self.button_background_color}
        {self.button_border_type}
        border-top-color : {self.button_background_color_name}
        border-bottom-color : {self.button_background_color_name}
        {self.button_border_color_right}
        {self.button_border_color_left}
        {self.button_border_curves}

        """)
        self.button_line.setIconSize(QSize(self.main_window_icon_size, self.main_window_icon_size + self.main_window_icon_height_offsett))

        self.button_shape.setIcon(QIcon("Images/Exo_Pen_Shapes_Large.png"))
        self.button_shape.setStyleSheet(
        f"""

        {self.button_background_color}
        {self.button_border_type}
        border-top-color : {self.button_background_color_name}
        border-bottom-color : {self.button_background_color_name}
        {self.button_border_color_right}
        {self.button_border_color_left}
        {self.button_border_curves}

        """)
        self.button_shape.setIconSize(QSize(self.main_window_icon_size, self.main_window_icon_size + self.main_window_icon_height_offsett))

        self.button_whiteboard.setIcon(QIcon("Images/Exo_Pen_Board_Logo_Large.png"))
        self.button_whiteboard.setStyleSheet(
        f"""

        {self.button_background_color}
        {self.button_border_type}
        border-top-color : {self.button_background_color_name}
        border-bottom-color : {self.button_background_color_name}
        {self.button_border_color_right}
        {self.button_border_color_left}
        {self.button_border_curves}

        """)
        self.button_whiteboard.setIconSize(QSize(self.main_window_icon_size, self.main_window_icon_size + self.main_window_icon_height_offsett))

        self.button_eraser.setIcon(QIcon("Images/Exo_Pen_Eraser_Logo.png"))
        self.button_eraser.setStyleSheet(
        f"""

        {self.button_background_color}
        {self.button_border_type}
        border-top-color : {self.button_background_color_name}
        border-bottom-color : {self.button_background_color_name}
        {self.button_border_color_right}
        {self.button_border_color_left}
        {self.button_border_curves}

        """)
        self.button_eraser.setIconSize(QSize(self.main_window_icon_size, self.main_window_icon_size + self.main_window_icon_height_offsett))

        self.button_settings.setIcon(QIcon("Images/Exo_Pen_Settings_Logo.png"))
        self.button_settings.setStyleSheet(
        f"""

        {self.button_background_color}
        {self.button_border_type}
        border-top-color : {self.button_background_color_name}
        border-bottom-color : {self.button_background_color_name}
        {self.button_border_color_right}
        {self.button_border_color_left}
        {self.button_border_curves}

        """)
        self.button_settings.setIconSize(QSize(self.main_window_icon_size, self.main_window_icon_size + self.main_window_icon_height_offsett))

        self.button_clear.setIcon(QIcon("Images/Exo_Pen_Clear_Logo_Large.png"))
        self.button_clear.setStyleSheet(
        f"""

        {self.button_background_color}
        {self.button_border_type}
        border-top-color : {self.button_background_color_name}
        border-bottom-color : {self.button_background_color_name}
        {self.button_border_color_right}
        {self.button_border_color_left}
        {self.button_border_curves}

        """)
        self.button_clear.setIconSize(QSize(self.main_window_icon_size, self.main_window_icon_size + self.main_window_icon_height_offsett))

        self.button_color.setMinimumSize(self.main_window_icon_size, self.main_window_icon_size + self.main_window_icon_height_offsett)
        self.button_color.setStyleSheet(
        f"""


        background-color : black;
        {self.button_border_type}
        {self.button_border_color_up}
        {self.button_border_color_down}
        {self.button_border_color_right}
        {self.button_border_color_left}
        {self.button_border_curves}

        """)

        #endregion

        #region Tray Properties
        self.tray.setIcon(QIcon("Images/Exo_Pen_LogoV1.png"))
        self.tray.setVisible(True)

        self.tray_menu_show.triggered.connect(self.TrayMenuShow)
        self.tray_menu_minimize.triggered.connect(self.TrayMenuMinimize)
        self.tray_menu_exit.triggered.connect(self.TrayMenuExit)
        self.tray.setContextMenu(self.tray_menu)
        
        #endregion


        #endregion


        #region TODO[epic=LayoutCreation] Setting Layout And Window Settings

        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlag(QtCore.Qt.Tool)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_X11NetWmWindowTypeDock)

        #endregion

        #endregion

        self.show()
    
    #region Functions

    #region TODO[epic=Functions] Menu Button Functioons

    def OnButtonMouseClick(self):
        print("Hi")
    
    def OnButtonPenClick(self):

        self.sub_window.showFullScreen()

        self.raise_()

    def OnButtonLineClick(self):
        pass

    def OnButtonShapeClick(self):
        pass

    def OnButtonWhiteboardClick(self):
        pass

    def OnButtonEraserClick(self):
        pass

    def OnButtonClearClick(self):
        pass

    def OnButtonSettingsClick(self):
        pass

    def OnButtonColorClick(self):
        pass

    #endregion

    #region TODO[epic=Functions] TrayButtonFunctions

    def TrayMenuMinimize(self):
        self.showMinimized()

    def TrayMenuShow(self):
        self.showNormal()

    def TrayMenuExit(self):
        app.quit()
    
    #endregion

    #region TODO[epic=Functions] MouseEvents
    #FIXME[epic=Functions] Need to stop the window when going out of the side 
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.move_label.underMouse():
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    #endregion

    #region TODO[epic=Functions] Run Functions

    def OnSubWindowClicked(self):
        self.raise_()

    #endregion

    #endregion

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())