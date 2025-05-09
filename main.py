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
        
        # Pegar a data
        self.ui.calendario.selectionChanged.connect(self.info_data)
        
        # Opções de pesquisas
        self.ui.check_nome.clicked.connect(self.pesquisa_nome)
        self.ui.check_cpf.clicked.connect(self.pesquisa_cpf)
        self.ui.check_num_consultorio.clicked.connect(self.pesquisa_consultorio)
        self.ui.check_contato.clicked.connect(self.pesquisa_contato)
                
    # Colocar a data
    def info_data(self):
        data_selecionada = self.ui.calendario.selectedDate()
        self.ui.date1.setDate(data_selecionada)
        
    # Opções de pesquisa
    def pesquisa_nome(self):
        
        # Desativar as outras CheckBox
        self.ui.check_cpf.setChecked(False)
        self.ui.check_num_consultorio.setChecked(False)
        self.ui.check_contato.setChecked(False)
    
    def pesquisa_cpf(self):
        
        # Desativar as outras CheckBox
        self.ui.check_nome.setChecked(False)
        self.ui.check_num_consultorio.setChecked(False)
        self.ui.check_contato.setChecked(False)
    
    def pesquisa_consultorio(self):
        
        # Desativar as outras CheckBox
        self.ui.check_nome.setChecked(False)
        self.ui.check_cpf.setChecked(False)
        self.ui.check_contato.setChecked(False)
    
    def pesquisa_contato(self):
        
        # Desativar as outras CheckBox
        self.ui.check_nome.setChecked(False)
        self.ui.check_cpf.setChecked(False)
        self.ui.check_num_consultorio.setChecked(False)
        
# Janela de Admin
class mainadmin(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainadmin, self).__init__()
        self.ui = Ui_MainAdmin()
        self.ui.setupUi(self)
        
        # Troca de paginas                                        
        self.ui.btn_agendamentos.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.pg_agendamentos))
        self.ui.btn_cadastro_users.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.pg_cadastro_users))
        
        # Escolha entre Paciente e Funcionario
        self.ui.check_normal.clicked.connect(self.prioradide_user)
        self.ui.check_admin.clicked.connect(self.prioradide_admin)
                
        # Pegar a data
        self.ui.calendario.selectionChanged.connect(self.info_data)

    # Alterar entre as checkbox paciente e funcionario
    def prioradide_user(self):
        self.ui.check_admin.setChecked(False)
        
    def prioradide_admin(self):
        self.ui.check_normal.setChecked(False)
            
    # Colocar a data
    def info_data(self):
        data_selecionada = self.ui.calendario.selectedDate()
        self.ui.date.setDate(data_selecionada)
        self.ui.date_2.setDate(data_selecionada)

# Starter
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    janela_login = login()
    janela_login.show()
    sys.exit(app.exec_())