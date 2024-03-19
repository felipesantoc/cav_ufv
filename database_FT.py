import sqlite3
from qgis.core import *
from qgis.PyQt.QtCore import QStandardPaths

class Data_base_FT:

    def __init__(self, name= str(QStandardPaths.standardLocations(QStandardPaths.AppDataLocation)[0]
                                 + '/profiles/default/python/plugins/cav/banco_ficha.db')) -> None:
        self.name = name
        # self.connection = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def criar_tabela_FT(self):
        # cria a tabela de ficha tecnica
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Ficha_tecnica(

            ID INTEGER NOT NULL,
            FT00 TEXT,
            FT01 TEXT,
            FT02 TEXT,
            FT03 TEXT,
            FT04 TEXT,
            FT05 TEXT,
            FT06 TEXT,
            FT07 TEXT,
            FT08 TEXT,
            FT09 TEXT,
            FT10 TEXT,
            FT11 TEXT,
            FT12 TEXT,
            FT13 TEXT,
            FT14 TEXT,
            FT15 TEXT,
            FT16 TEXT,
            FT17 TEXT,
            FT18 TEXT,
            FT19 TEXT,
            FT20 TEXT,
            FT21 TEXT,
            FT22 TEXT,
            FT23 TEXT,
            FT24 TEXT,
            FT25 TEXT,
            FT26 TEXT,
            FT27 TEXT,
            FT28 TEXT,
            FT29 TEXT,
            FT30 TEXT,


            PRIMARY KEY(ID AUTOINCREMENT)
            );


        """)

    def cadastrar_FT(self, ficha):

        campos_tabela = ('FT00', 'FT01', 'FT02', 'FT03', 'FT04', 'FT05', 'FT06', 'FT07', 'FT08', 'FT09', 'FT10',
                         'FT11', 'FT12', 'FT13', 'FT14', 'FT15', 'FT16', 'FT17', 'FT18', 'FT19', 'FT20',
                         'FT21', 'FT22', 'FT23', 'FT24', 'FT25', 'FT26', 'FT27', 'FT28', 'FT29', 'FT30')

        qntd = ("?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Ficha_tecnica {campos_tabela}
            VALUES({qntd})""", ficha)
            self.connection.commit()
            return ("OK")

        except Exception as e:
            return e

    def select_all_FT(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Ficha_tecnica ORDER BY ID")
            reservatorios = cursor.fetchall()
            return reservatorios
        except:
            pass

    def delete_FT(self, id):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Ficha_tecnica WHERE ID = '{id}' ")

            self.connection.commit()

            return "Cadastro do reservatório excluido com sucesso!"

        except:
            return "Erro ao Excluir registro!"

    def update_FT(self, fullDataSet):

        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE Ficha_tecnica set

            ID = '{fullDataSet[0]}',
            FT00 = '{fullDataSet[1]}',
            FT01 = '{fullDataSet[2]}',
            FT02 = '{fullDataSet[3]}',
            FT03 = '{fullDataSet[4]}',
            FT04 = '{fullDataSet[5]}',
            FT05 = '{fullDataSet[6]}',
            FT06 = '{fullDataSet[7]}',
            FT07 = '{fullDataSet[8]}',
            FT08 = '{fullDataSet[9]}',
            FT09 = '{fullDataSet[10]}',
            FT10 = '{fullDataSet[11]}',
            FT11 = '{fullDataSet[12]}',
            FT12 = '{fullDataSet[13]}',
            FT13 = '{fullDataSet[14]}',
            FT14 = '{fullDataSet[15]}',
            FT15 = '{fullDataSet[16]}',
            FT16 = '{fullDataSet[17]}',
            FT17 = '{fullDataSet[18]}',
            FT18 = '{fullDataSet[19]}',
            FT19 = '{fullDataSet[20]}',
            FT20 = '{fullDataSet[21]}',
            FT21 = '{fullDataSet[22]}',
            FT22 = '{fullDataSet[23]}',
            FT23 = '{fullDataSet[24]}',
            FT24 = '{fullDataSet[25]}',
            FT25 = '{fullDataSet[26]}',
            FT26 = '{fullDataSet[27]}',
            FT27 = '{fullDataSet[28]}',
            FT28 = '{fullDataSet[29]}',
            FT29 = '{fullDataSet[30]}',
            FT30 = '{fullDataSet[31]}'
            
           

            WHERE ID = '{fullDataSet[0]}'""")

        self.connection.commit()
