import sqlite3

import PyQt5.QtSql
from PyQt5 import QtWidgets
import sys



class ShipTable:
    def __init__(self, serial_no, name, weight, product_year, ship_type):
        '''Alınacak bilgilerin nesnelerini oluşturma'''
        self.serial_no = serial_no
        self.name = name
        self.weight = weight
        self.product_year = product_year
        self.ship_type = ship_type

        self.create_connect()

    def create_connect(self):
        '''Tablonun sql kodu ile oluşturulması'''
        self.connect = sqlite3.connect("Odev2.db")     # veri tabanına bağlanma
        self.cursor = self.connect.cursor()

        table = "CREATE TABLE IF NOT EXISTS SHIPS(" \
                "SERIAL_NO INTEGER PRIMARY KEY UNIQUE, " \
                "NAME TEXT NOT NULL, " \
                "WEIGHT FLOAT NOT NULL, " \
                "PRODUCT_YEAR INTEGER NOT NULL," \
                "SHIP_TYPE TEXT NOT NULL)"

        self.cursor.execute(table)
        self.connect.commit()                           # veri tabanındaki değişikleri kaydetme


class CruiseShip(ShipTable):
    def __init__(self, serial_no, name, weight, product_year, ship_type, ship_capacity):
        super().__init__(serial_no, name, weight, product_year, ship_type)
        '''Kalıtım ile alınmayanların alınacak bilgilerin, nesnelerini oluşturulma'''
        self.ship_capacity = ship_capacity

        self.create_connect()

    def create_connect(self):
        '''Tablonun sql kodu ile oluşturulması'''
        self.connect = sqlite3.connect("Odev2.db")     # veri tabanına bağlanma
        self.cursor = self.connect.cursor()

        table = "CREATE TABLE IF NOT EXISTS CRUISE_SHIP(" \
                "SHIP_SERIAL_NO INTEGER PRIMARY KEY UNIQUE," \
                "SHIP_CAPACITY INTEGER NOT NULL, " \
                "FOREIGN KEY (SHIP_SERIAL_NO) REFERENCES SHIPS(SERIAL_NO))"

        self.cursor.execute(table)
        self.connect.commit()                           # veri tabanındaki değişikleri kaydetme



class OilShip(ShipTable):
    def __init__(self, serial_no, name, weight, product_year, ship_type, ship_oil_capacity):
        '''Kalıtım ile alınmayanların alınacak bilgilerin, nesnelerini oluşturulma'''
        super().__init__(serial_no, name, weight, product_year, ship_type)
        self.ship_oil_capacity = ship_oil_capacity

        self.create_connect()

    def create_connect(self):
        '''Tablonun sql kodu ile oluşturulması'''
        self.connect = sqlite3.connect("Odev2.db")     # veri tabanına bağlanma
        self.cursor = self.connect.cursor()

        table = "CREATE TABLE IF NOT EXISTS OIL_SHIP(" \
                "SHIP_SERIAL_NO INTEGER PRIMARY KEY UNIQUE," \
                "SHIP_OIL_CAPACITY INTEGER NOT NULL, " \
                "FOREIGN KEY (SHIP_SERIAL_NO) REFERENCES SHIPS(SERIAL_NO))"

        self.cursor.execute(table)
        self.connect.commit()                           # veri tabanındaki değişikleri kaydetme


class ContainerShip(ShipTable):
    def __init__(self, serial_no, name, weight, product_year, ship_type, ship_max_capacity, ship_container_amount):
        '''Alınacak bilgilerin nesnelerini kalıtım ile alınmayanların oluşturulma'''
        super().__init__(serial_no, name, weight, product_year, ship_type)
        self.ship_max_capacity = ship_max_capacity
        self.ship_container_amount = ship_container_amount

        self.create_connect()

    def create_connect(self):
        '''Tablonun sql kodu ile oluşturulması'''
        self.connect = sqlite3.connect("Odev2.db")     # veri tabanına bağlanma
        self.cursor = self.connect.cursor()

        table = "CREATE TABLE IF NOT EXISTS CONTAINER_SHIP(" \
                "SHIP_SERIAL_NO INTEGER PRIMARY KEY UNIQUE," \
                "SHIP_CONTAINER_AMOUNT INTEGER NOT NULL, " \
                "SHIP_MAX_CAPACITY INTEGER NOT NULL," \
                "FOREIGN KEY (SHIP_SERIAL_NO) REFERENCES SHIPS(SERIAL_NO))"

        self.cursor.execute(table)
        self.connect.commit()                           # veri tabanındaki değişikleri kaydetme


class VoyageTable:
    def __init__(self, ID, takeoff_date, return_date, takeoff_place, serial_no):
        '''Alınacak bilgilerin nesnelerini oluşturma'''
        self.ID = ID
        self.takeoff_date = takeoff_date
        self.return_date = return_date
        self.takeoff_place = takeoff_place
        self.serial_no = serial_no

        self.create_connect()

    def create_connect(self):
        '''Tablonun sql kodu ile oluşturulması'''
        self.connect = sqlite3.connect("Odev2.db")     # veri tabanına bağlanma
        self.cursor = self.connect.cursor()

        table = "CREATE TABLE IF NOT EXISTS VOYAGES(" \
                "ID INTEGER UNIQUE," \
                "TAKEOFF_DATE TEXT NOT NULL," \
                "RETURN_DATE TEXT NOT NULL," \
                "TAKEOFF_PLACE TEXT NOT NULL," \
                "SERIAL_NO INTEGER NOT NULL," \
                "CAP INTEGER NOT NULL," \
                "CREW INTEGER NOT NULL," \
                "FOREIGN KEY(SERIAL_NO) REFERENCES SHIPS(SERIAL_NO)," \
                "CONSTRAINT DATE_CHECK UNIQUE(SERIAL_NO, TAKEOFF_DATE, TAKEOFF_PLACE)," \
                "CONSTRAINT COUNT_CHECK CHECK(CAP >= 2), CHECK(CREW >= 1)," \
                "PRIMARY KEY (ID))"

        self.cursor.execute(table)
        self.connect.commit()                           # veri tabanındaki değişikleri kaydetme


class Harbors:
    def __init__(self, harbour_name, country, population, passport, billcost):
        '''Alınacak bilgilerin nesnelerini oluşturma'''
        self.harbour_name = harbour_name
        self.country = country
        self.population = population
        self.passport = passport
        self.billcost = billcost

        self.create_connect()

    def create_connect(self):
        '''Tablonun sql kodu ile oluşturulması'''
        self.connect = sqlite3.connect("Odev2.db")     # veri tabanına bağlanma
        self.cursor = self.connect.cursor()

        table = "CREATE TABLE IF NOT EXISTS HARBORS(" \
                "HARBOUR_NAME TEXT NOT NULL," \
                "COUNTRY TEXT NOT NULL," \
                "POPULATION INTEGER NOT NULL," \
                "PASSPORT INTEGER NOT NULL," \
                "BILLCOST INTEGER NOT NULL," \
                "PRIMARY KEY(HARBOUR_NAME, COUNTRY))"

        self.cursor.execute(table)
        self.connect.commit()                           # veri tabanındaki değişikleri kaydetme


class VisitedHarbour:
    def __init__(self, harbour_name, harbour_country, serial_no):
        '''Alınacak bilgilerin nesnelerini oluşturma'''
        self.harbour_name = harbour_name
        self.harbour_country = harbour_country
        self.serial_no = serial_no

        self.create_connect()

    def create_connect(self):
        '''Tablonun sql kodu ile oluşturulması'''
        self.connect = sqlite3.connect("Odev2.db")     # veri tabanına bağlanma
        self.cursor = self.connect.cursor()

        table = "CREATE TABLE IF NOT EXISTS VISITED_HARBOURS(" \
                "HARBOUR_NAME TEXT NOT NULL," \
                "HARBOUR_COUNTRY TEXT NOT NULL," \
                "SERIAL_NO INTEGER NOT NULL," \
                "PRIMARY KEY(SERIAL_NO)," \
                "FOREIGN KEY(HARBOUR_NAME,HARBOUR_COUNTRY) REFERENCES HARBORS(HARBOUR_NAME,COUNTRY)," \
                "FOREIGN KEY(SERIAL_NO) REFERENCES SHIPS(SERIAL_NO))"

        self.cursor.execute(table)
        self.connect.commit()                           # veri tabanındaki değişikleri kaydetme



class Captains:
    def __init__(self, ID, name, surname, address, citizenship, birth_date, date_of_recruitment, license):
        '''Alınacak bilgilerin nesnelerini oluşturma'''
        self.ID = ID
        self.name = name
        self.surname = surname
        self.address = address
        self.citizenship = citizenship
        self.birth_date = birth_date
        self.date_of_recruitment = date_of_recruitment
        self.license = license

        self.create_connect()

    def create_connect(self):
        '''Tablonun sql kodu ile oluşturulması'''
        self.connect = sqlite3.connect("Odev2.db")     # veri tabanına bağlanma
        self.cursor = self.connect.cursor()

        table = "CREATE TABLE IF NOT EXISTS CAPTAINS(" \
                "ID INTEGER PRIMARY KEY," \
                "NAME TEXT NULL," \
                "SURNAME TEXT NULL," \
                "ADDRESS TEXT NULL," \
                "CITIZENSHIP TEXT NULL," \
                "BIRTH_DATE TEXT NULL," \
                "DATE_OF_RECRUITMENT TEXT NULL," \
                "LICENSE TEXT)"

        self.cursor.execute(table)
        self.connect.commit()                           # veri tabanındaki değişikleri kaydetme


class CrewMembers(Captains):
    def __init__(self, ID, name, surname, address, citizenship, birth_date, date_of_recruitment, mission, license):
        '''Alınacak bilgilerin nesnelerini oluşturma'''
        super().__init__(ID, name, surname, address, citizenship, birth_date, date_of_recruitment,license)
        self.mission = mission

        self.create_connect()

    def create_connect(self):
        '''Tablonun sql kodu ile oluşturulması'''
        self.connect = sqlite3.connect("Odev2.db")     # veri tabanına bağlanma
        self.cursor = self.connect.cursor()

        table = "CREATE TABLE IF NOT EXISTS CREW_MEMBERS(" \
                "ID INTEGER PRIMARY KEY," \
                "NAME TEXT NULL," \
                "SURNAME TEXT NULL," \
                "ADDRESS TEXT NULL," \
                "CITIZENSHIP TEXT NULL," \
                "BIRTH_DATE TEXT NULL," \
                "DATE_OF_RECRUITMENT TEXT NULL," \
                "MISSION TEXT)"

        self.cursor.execute(table)
        self.connect.commit()                           # veri tabanındaki değişikleri kaydetme


##################################  ARAYÜZ KODU ##################################

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Veritabanı Tabloları")

        try:
            self.db = PyQt5.QtSql.QSqlDatabase("QSQLITE")
            self.db.setDatabaseName("Odev2.db")
            if not self.db.open():
                raise Exception(self.db.lastError().text())
        except Exception as e:
            print(f"Veritabanı bağlantısı başarısız oldu.\n Hata kodu: {e}")

        ship_table = ShipTable
        ship_table.create_connect(self)

        cruise_ship = CruiseShip
        cruise_ship.create_connect(self)

        oil_ship = OilShip
        oil_ship.create_connect(self)

        container_ship = ContainerShip
        container_ship.create_connect(self)

        voyage_table = VoyageTable
        voyage_table.create_connect(self)

        harbor = Harbors
        harbor.create_connect(self)

        visited_harbor = VisitedHarbour
        visited_harbor.create_connect(self)

        captain = Captains
        captain.create_connect(self)

        crew_members = CrewMembers               # sınıfların nesnesini oluşturup
        crew_members.create_connect(self)        # nesneler üzerinden sınıfları çağırma

        main_layout = QtWidgets.QVBoxLayout()    # layout(dikey düzen) oluşturma

        table_layout = QtWidgets.QHBoxLayout()   # layout(yatay düzen) oluşturma

        self.table_combobox = QtWidgets.QComboBox()  # comboBox oluşturma
        self.table_combobox.currentIndexChanged.connect(self.on_combobox_index_changed)
        table_layout.addWidget(self.table_combobox)

        self.text_edit = QtWidgets.QTextEdit()       # TableView oluşturun
        self.text_edit.setReadOnly(True)             # text_Edit alanı sadece çıktı gösterme alanı şeklinde ayarlama
        table_layout.addWidget(self.text_edit)

        main_layout.addLayout(table_layout)

        tables = self.db.tables()                    # Veritabanındaki tabloları çekip listeye atmak
        for table in tables:
            self.table_combobox.addItem(table)       # comboBox'a eklemek


        button_layout = QtWidgets.QHBoxLayout()      # layout oluşturup buton eklemek
        self.button_adding_to_table = QtWidgets.QPushButton("EKLEME")
        self.button_remove_to_table = QtWidgets.QPushButton("SİLME")
        self.button_editing_to_table = QtWidgets.QPushButton("DÜZENLEME")

        button_layout.addWidget(self.button_adding_to_table)
        button_layout.addWidget(self.button_remove_to_table)
        button_layout.addWidget(self.button_editing_to_table)

        self.button_adding_to_table.clicked.connect(self.adding)        # butona tıklandığında çağırılan fonksiyon
        self.button_remove_to_table.clicked.connect(self.removing)
        self.button_editing_to_table.clicked.connect(self.editing)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def populate_text_edit(self, data, cursor):
        '''Populate text edit area with data'''
        header = [description[0] for description in cursor.description]
        self.text_edit.setPlainText('\t'.join(header) + '\n')
        for row in data:
            self.text_edit.append('\t'.join(map(str, row)))


    def on_combobox_index_changed(self, index):
        '''Showing to chosen table in database'''
        selected_table = self.db.tables()[index]
        db = sqlite3.connect("odev2.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {selected_table}")
        veriler = cursor.fetchall()
        db.close()

        self.populate_text_edit(veriler, cursor)

    def adding(self):
        '''Calling adding class'''
        add_data_dialog = AddDataDialog()
        add_data_dialog.exec_()
        # add_data_dialog.close()

    def removing(self):
        ''' and calling remove class'''
        table_name, ok = QtWidgets.QInputDialog.getText(self, "Tablo Seçimi", f"{[i for i in self.db.tables()]}"
                                                                              f"\nTablo Adı:")
        if ok:
            self.remove_data_dialog = DeleteDataDialog(table_name.upper())
            self.remove_data_dialog.exec_()

    def editing(self):
        '''Calling '''
        table_name, ok = QtWidgets.QInputDialog.getText(self, "Tablo Seçimi", f"{[i for i in self.db.tables()]}"
                                                                              f"\nTablo Adı:")
        if ok:
            self.update_data_dialog = UpgradeDataDialog(table_name.upper())
            self.update_data_dialog.exec_()


class AddDataDialog(QtWidgets.QDialog):
    '''Adding class'''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Veri Ekle")

        self.layout = QtWidgets.QVBoxLayout()

        self.table_combobox = QtWidgets.QComboBox()
        self.populate_table_combobox()
        self.layout.addWidget(self.table_combobox)

        self.column_layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.column_layout)

        self.add_row_button = QtWidgets.QPushButton("Satır Ekle")
        self.add_row_button.clicked.connect(self.add_row)
        self.layout.addWidget(self.add_row_button)

        self.submit_button = QtWidgets.QPushButton("Ekle")
        self.submit_button.clicked.connect(self.add_data)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

        self.data = {}

    def populate_table_combobox(self):
        '''Adding tables in databese'''
        self.db = sqlite3.connect("odev2.db")
        cursor = self.db.cursor()

        cursor.execute("Select name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()      # bir sorgulama yapar ve bu sorgulamada sqlite_master ile
        for table in tables:            # veritabanındaki bütün nesneleri alır ama type=table ile sadece
            self.table_combobox.addItem(table[0])   # table nesnesini alır ve bu nesneleri tuple olarak aldığı için comboboxa eklenen
                                        # isim eklendiği için sadece table[0] kullanır

    def add_row(self):
        # tablo sütunlarını al
        table_name = self.table_combobox.currentText()
        cursor = self.db.cursor()
        cursor.execute(f"PRAGMA table_info({table_name});")
        # pragma sorgusu sqlite özelliği ve otomatik olarak veri tabanına ayrıntı sağlar
        columns = cursor.fetchall()
        row_layout = QtWidgets.QHBoxLayout()
        for column in columns:
            label = QtWidgets.QLabel(column[1])
            line_edit = QtWidgets.QLineEdit()
            row_layout.addWidget(label)
            row_layout.addWidget(line_edit)
            self.data[column[1]] = line_edit
        self.column_layout.addLayout(row_layout)


    def add_data(self):
        # Tabloya veri ekle
        table_name = self.table_combobox.currentText()
        data_values = [self.data[column].text() for column in self.data]
        # Veritabanına ekleme işlemi
        try:
            self.db.execute(f"INSERT INTO {table_name} VALUES ({','.join(['?'] * len(data_values))})", data_values)
            self.db.commit()
            QtWidgets.QMessageBox.information(self, "Bilgi", "Veri başarıyla eklendi.")
            QtWidgets.QMessageBox.close(self)
            QtWidgets.QDialog.close(self)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Uyarı", f"Veri eklenirken bir hata oluştu: {str(e)}")


class DeleteDataDialog(QtWidgets.QDialog):
    '''Delete class'''
    def __init__(self, table_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Veri Silme")
        self.table_name = table_name

        self.layout = QtWidgets.QVBoxLayout()

        self.text_edit = QtWidgets.QTextEdit()        # çıktı alanı(text_Edit) alanı oluşturma
        self.text_edit.setReadOnly(True)              # text_Edit alanı sadece çıktı gösterme alanı şeklinde ayarlama
        self.populate_text_edit()
        self.layout.addWidget(self.text_edit)

        columns = self.get_table_columns()
        self.first_column_name = columns[0] if columns else None

        label = QtWidgets.QLabel(f"{self.first_column_name}")
        self.linedit = QtWidgets.QLineEdit()
        self.layout.addWidget(label)
        self.layout.addWidget(self.linedit)

        self.delete_button = QtWidgets.QPushButton("Satırı Sil")
        self.delete_button.clicked.connect(self.delete_row)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

    def get_table_columns(self):
        connection = sqlite3.connect("odev2.db")
        cursor = connection.cursor()
        cursor.execute(f"PRAGMA table_info({self.table_name})")
        columns = cursor.fetchall()
        connection.close()
        return [column[1] for column in columns]

    def populate_text_edit(self):
        try:
            db = sqlite3.connect("Odev2.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM {self.table_name}")
            data = cursor.fetchall()
            header = [description[0] for description in cursor.description]
            self.text_edit.setPlainText('\t'.join(header) + '\n')
            for row in data:
                self.text_edit.append('\t'.join(map(str, row)))
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Hata", f"Veri tabanı hatası: {str(e)}")

    def delete_row(self):
        try:
            db = sqlite3.connect("Odev2.db")
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM {self.table_name} WHERE {self.first_column_name} = ?", (self.linedit.text(),))
            db.commit()
            QtWidgets.QMessageBox.information(self, "Başarılı", "Satır başarıyla silindi.")
            self.close()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Hata", f"Hata oluştu: {str(e)}")


class UpgradeDataDialog(QtWidgets.QDialog):
    '''Update class'''
    def __init__(self, table_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Veri Düzeltme")
        self.table_name = table_name

        self.layout = QtWidgets.QVBoxLayout()

        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setReadOnly(True)              # text_Edit alanı sadece çıktı gösterme alanı şeklinde ayarlama
        self.populate_text_edit()
        self.layout.addWidget(self.text_edit)

        columns = self.get_table_columns()
        self.first_column_name = columns[0] if columns else None      # tablo sütunlarını bir listeye atıp onun ilk elemanını çağırmak

        label = QtWidgets.QLabel(f"Güncellemek istenilen satırın {self.first_column_name}: ")
        self.linedit = QtWidgets.QLineEdit()
        update_label = QtWidgets.QLabel(f"Güncellemek istenilen sütun ismi: ")
        self.linedit1 = QtWidgets.QLineEdit()
        update_label_data = QtWidgets.QLabel(f"Sütuna kaydedilecek yeni veri: ")
        self.linedit2 = QtWidgets.QLineEdit()

        self.layout.addWidget(label)
        self.layout.addWidget(self.linedit)
        self.layout.addWidget(update_label)
        self.layout.addWidget(self.linedit1)
        self.layout.addWidget(update_label_data)
        self.layout.addWidget(self.linedit2)

        self.edit_button = QtWidgets.QPushButton("Satırı Düzelt")
        self.edit_button.clicked.connect(self.update_data)
        self.layout.addWidget(self.edit_button)

        self.setLayout(self.layout)

    def get_table_columns(self):
        '''Tablo sütunlarını alan fonksiyon'''
        connection = sqlite3.connect("odev2.db")
        cursor = connection.cursor()
        cursor.execute(f"PRAGMA table_info({self.table_name})")
        columns = cursor.fetchall()
        connection.close()
        return [column[1] for column in columns]

    def populate_text_edit(self):
        '''Text_edit alanına yazılan fonksiyon'''
        try:
            db = sqlite3.connect("Odev2.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM {self.table_name}")
            data = cursor.fetchall()
            header = [description[0] for description in cursor.description]
            self.text_edit.setPlainText('\t'.join(header) + '\n')
            for row in data:
                self.text_edit.append('\t'.join(map(str, row)))
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Hata", f"Veri tabanı hatası: {str(e)}")

    def update_data(self):
        '''Verileri güncelleyen fonksiyon'''
        try:
            db = sqlite3.connect("Odev2.db")
            cursor = db.cursor()
            cursor.execute(f"UPDATE {self.table_name} SET {self.linedit1.text().upper()} = ? WHERE {self.first_column_name} = ?", (self.linedit2.text(), self.linedit.text(),))

            db.commit()
            QtWidgets.QMessageBox.information(self, "Başarılı", "Satır başarıyla güncellendi.")
            self.close()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Hata", f"Hata oluştu: {str(e)}")

if __name__ == "__main__":
    '''Bütün kodu ana fonksiyona yani ana sınıfa, arayüze bağlayıp burda o sınıfı çağırma yapıyoruz'''
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
