class Bem_Vindo:
    def __init__ (self):
        self.nome = input("qual é o seu nome? ")
        self.msg = print(f"Olá {self.nome}, seja muito bem vindo aos juros compostos! Aqui nós cuidamos da sua aposentadoria :)")

    def msg_bem_vindo(self):
        print(self.msg)

    def perguntas_iniciais (self):
        self.dinheiro_inicial = int(input("Digite a quantidade de dinheiro inicial do investimento: "))
        self.tempo = int(input("Digite quantos anos você deixará o dinheiro investido: "))
        self.taxa = float(input("Digite, em decimal, qual a taxa anual de retorno do se investimento: "))

class Calculadora (Bem_Vindo):
    def calc_investimento (self):
        montante = self.dinheiro_inicial * (1 + self.taxa) ** self.tempo
        montante = round(montante,2)
        print("------------------------------------------------")
        print(f"Parabéns {self.nome}! Ao final do período você terá R${montante}!")


# Criação de instâncias e chamadas dos métodos
calc = Calculadora()
calc.msg_bem_vindo()
calc.perguntas_iniciais()
calc.calc_investimento()