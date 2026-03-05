# aqui é onde fica o menu do totem, ou seja, as opções de atendimento

class Menu:
    def __init__(self):
        self.menu = {
        1: "atendimento",
        2: "atendimento preferencial",
        3: "atendimento 80 anos ou mais",
        }

def exibir(self):
        #exibir o menu de serviços
        print("\n" + "="*30)
        print("        MENU DE SERVIÇOS        ")
        print("="*30)
        for chave, descricao in self.servicos.items():
            print(f" [{chave}] {descricao}")
        print("="*30)

def selecao(self):
    #selecionar o serviço desejado
    while True:
        try:
            escolha = int(input("Selecione o atendimento desejado: "))
            if escolha in self.servicos:
                print(f"\nVocê selecionou: {self.servicos[escolha]}")
                return escolha
            else:
                print("Opção inválida. Por favor, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

