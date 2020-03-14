from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import MS5637 as sensorMS

pressure = sensorMS.pressure
temp_M = sensorMS.cTemp
temp_f_M = sensorMS.fTemp

headers = ["Measurement","Si7021", "MS5637"]
rows = [("Temperature in Celsius", "1643-01-04", temp_M),
        ("Temperature in Fahrenheit", "1643-01-04", temp_f_M),
        ("Humidity %%RH", "1643-01-04", "Classical mechanics"),
        ("Altitude", "1879-03-14", "Relativity"),
        ("Pressure", "1809-02-12", pressure)]

class TableModel(QAbstractTableModel):
    def rowCount(self, parent):
        return len(rows)
    def columnCount(self, parent):
        return len(headers)
    def data(self, index, role):
        if role != Qt.DisplayRole:
            return QVariant()
        return rows[index.row()][index.column()]
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        return headers[section]

app = QApplication(["Sensors"])
model = TableModel()
view = QTableView()
view.setGeometry(100,400,400,200)
view.setModel(model)
view.show()
app.exec_()