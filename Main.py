from UI import *
from ModModel import *
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


def table(lst):
    numrows = len(lst)
    numcols = len(lst[0])
    ui_main.tableWidget.setColumnCount(numcols)
    ui_main.tableWidget.setRowCount(numrows)
    lst = str(lst)
    for row in range(numrows):
        for column in range(numcols):
            ui_main.tableWidget.setItem(row, column, QTableWidgetItem((lst[row][column])))

def routes():
    print('Запущена функция Routes')
    first_city = ui_main.FirstCity.text()
    second_city = ui_main.SecondCity.text()
    lst = getroutes(first_city, second_city)
    '''Создание таблицы'''
    numrows = len(lst)
    numcols = len(lst[0])
    print(numcols, numrows)
    ui_main.tableRouts.setColumnCount(numcols)
    ui_main.tableRouts.setRowCount(numrows)
    for row in range(numrows):
        for column in range(numcols):
            ui_main.tableRouts.setItem(row, column, QTableWidgetItem(str(lst[row][column])))

    print('btn Search Pushed')
def search():
    min_lat = ui_main.MinLat.text()
    max_lat = ui_main.maxLat.text()
    min_lon = ui_main.minLon.text()
    max_lon = ui_main.lonMax.text()
    lst = getinfo(min_lat, max_lat, min_lon, max_lon)
    '''Создание таблицы'''
    numrows = len(lst)
    numcols = len(lst[0])
    print(numcols, numrows)
    ui_main.tableWidget.setColumnCount(numcols)
    ui_main.tableWidget.setRowCount(numrows)
    for row in range(numrows):
        for column in range(numcols):
            ui_main.tableWidget.setItem(row, column, QTableWidgetItem(str(lst[row][column])))

    print('btn Search Pushed')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui_main = Ui_AirportApplication()
    ui_main.setupUi(main_window)
    ui_main.btnSearch.clicked.connect(search)
    ui_main.btnRouts.clicked.connect(routes)
    main_window.show()
    sys.exit(app.exec())