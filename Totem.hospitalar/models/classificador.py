class Classificador:
    def definir_prioridade(self, paciente):
        if paciente.idade >= 80:
            return "Super prioritário"
        elif paciente.idade >= 60 or paciente.pcd.lower() == "sim":
            return "Prioritário"
        else:
            return "Normal"