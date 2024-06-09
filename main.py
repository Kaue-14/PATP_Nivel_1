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
        self.ui.btn_login.clicked.connect(self.abrir_janelas)
    
    # Abrir as janelas main
    def abrir_janelas(self):
        # janela de main admin
        if self.ui.input_senha.text() == "admin" and self.ui.input_usuario.text() == "admin":
            self.m = mainadmin()
            self.m.show()
            self.close()
        # janela de main users
        elif self.ui.input_senha.text() == "user" and self.ui.input_usuario.text() == "user":
            self.u = mainusers()
            self.u.show()
            self.close()
        # bypass remover dps que finalizar
        else:
            # Janela users
            self.u = mainusers()
            self.u.show()
            self.close()
            # Janela admin
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
        
        # Troca de pagina ao selecionar data
        self.ui.calendario.selectionChanged.connect(lambda: self.ui.pages_users.setCurrentWidget(self.ui.pg_consultas))
        
        # Volta pra tela de login
        self.ui.voltar_login.clicked.connect(self.volta_login)
        
        # Pegar a data
        self.ui.calendario.selectionChanged.connect(self.info_data)
        
    # Volta pra tela de login
    def volta_login(self):
        self.l = login()
        self.l.show()
        self.close()
        
    # Colocar a data
    def info_data(self):
        data_selecionada = self.ui.calendario.selectedDate()
        self.ui.date1.setDate(data_selecionada)
        
# Janela de Admin
class mainadmin(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainadmin, self).__init__()
        self.ui = Ui_MainAdmin()
        self.ui.setupUi(self)
        
        # Troca de paginas                                        
        self.ui.btn_agendamentos.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.pg_agendamentos))
        self.ui.btn_cadastro_users.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.pg_cadastro_users))
        
        # Volta pra tela de login
        self.ui.voltar_login.clicked.connect(self.volta_login)
        
        # Pegar a data
        self.ui.calendario.selectionChanged.connect(self.info_data)
    
    # Colocar a data
    def info_data(self):
        data_selecionada = self.ui.calendario.selectedDate()
        self.ui.date.setDate(data_selecionada)

    # Volta pra tela de login
    def volta_login(self):
        self.l = login()
        self.l.show()
        self.close()

# Starter
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela_login = login()
    janela_login.show()
    sys.exit(app.exec_())