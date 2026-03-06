class gerador_senha:
    def __init__(self):
        # guardar a fila, iniando do 0
        self.gerador = {
            "G": 0,
            "P": 0,
            "SP": 0,
        }

    def gerarSenha(self, opcao_menu):
        # Só para salvar o código e mapealo de acordo com o prefixo, ou sla so para salvar
        mapa_prefixos = {
            1: "G",
            2: "P",
            3: "SP"
        }

        if opcao_menu in mapa_prefixos:
                    prefixo = mapa_prefixos[opcao_menu]
                #Aqui iniciamos o contador para o prefixo, se não existir, iniciamos com 0
                    self.gerador[prefixo] += 1
                #Formata para senhas genercas
                    numero_formatado = f"{self.gerador[prefixo]:03d}"
                    senha_final = f"{prefixo}-{numero_formatado}"
                    
                    return senha_final
        else:
            return None