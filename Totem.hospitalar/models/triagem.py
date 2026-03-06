class Triagem:
    def __init__(self, paciente, servico):
        self.paciente = paciente
        self.servico = servico

    def verificar(self):
        if self.servico == 3:
            print("\n------------------------------------------")
            print("ALERTA DE EMERGÊNCIA")
            print("------------------------------------------")
            print(f"PACIENTE: {self.paciente.nome}")
            print(">>> ENCAMINHAR IMEDIATAMENTE AO BOX MÉDICO")
            print("Não é necessário aguardar senha.")
            print("------------------------------------------")
            return True
        return False
    #WOIW