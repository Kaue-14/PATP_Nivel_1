from PyQt5 import QtWidgets
import sys

# Qt designer
from designer.login import Ui_Login
from designer.main_admin import Ui_MainAdmin
from designer.main_users import Ui_MainUsers

# Janela de Login
class login(QtWidgets.QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        # botão de login
        self.ui.btn_login.clicked.connect(self.abrir_admin_sempre)
    
    # Abrir as janelas main
    def abrir_admin_sempre(self):
        # janela de main admin
        if self.ui.input_senha.text() == "admin" and self.ui.input_usuario.text() == "admin":
            self.m = mainadmin()
            self.m.show()
            self.close()
        # janela de main users
        elif self.ui.input_senha.text() == "paciente" and self.ui.input_senha.text() == "paciente":
            self.m = mainusers()
            self.m.show()
            self.close()
        # bypass remover dps que finalizar
        else:
            self.m = mainadmin()
            self.m.show()
            self.close()

#  Janela de users
class mainusers(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainusers, self).__init__()
        self.ui = Ui_MainUsers()
        self.ui.setupUi(self)
        
        # Troca de paginas                                        
        self.ui.btn_calendario.clicked.connect(lambda: self.ui.pages_users.setCurrentWidget(self.ui.pg_calendario))
        self.ui.btn_consultas.clicked.connect(lambda: self.ui.pages_users.setCurrentWidget(self.ui.pg_consultas))
        
# Janela de Admin
class mainadmin(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainadmin, self).__init__()
        self.ui = Ui_MainAdmin()
        self.ui.setupUi(self)
        
        # Troca de paginas                                        
        self.ui.btn_agendamentos.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.pg_agendamentos))
        self.ui.btn_cadastro_users.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.pg_cadastro_users))
        
        # Pegar a data
        self.ui.calendario.selectionChanged.connect(self.info_data)
        
    def info_data(self):
        data_selecionada = self.ui.calendario.selectedDate()
        
        self.ui.date.setDate(data_selecionada)


# Starter
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela_login = login()
    janela_login.show()
    sys.exit(app.exec_())