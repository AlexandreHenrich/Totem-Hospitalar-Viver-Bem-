class classificador:
    def definir_prioridade(self,paciente):
        if paciente.idade >= 60 or paciente.pcd:
            return "Prioritário"
        if else paciente.idade <80:
            return "Super prioritário"
        else:
            return "Normal"