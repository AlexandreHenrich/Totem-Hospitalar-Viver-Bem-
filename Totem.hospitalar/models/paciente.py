#feat paciente 
#jao que fez tem felipe n 


class Pacientes:
    def __init__(self, nome, idade, pcd):
        self.nome = nome
        self.idade = idade
        self.pcd = pcd 
    
    def exibir_dados_paciente(self):
        status_pcd = "Sim" if self.pcd else "Não"
        return f"Nome: {self.nome} | Idade: {self.idade} | PCD: {status_pcd}"  
