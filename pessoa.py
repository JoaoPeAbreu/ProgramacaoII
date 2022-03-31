class Pessoa:

    def __init__(self, nome:str, email:str, numero:int):
        self.no = nome
        self.em = email
        self.nu = numero

    def informar(self):
        self.no = input("Digite o seu nome: ")
        self.em = input("Digite o seu e-mail: ")
        self.nu = input("Digite o seu numero de telefone: ")
        

if __name__ == "__main__":
    pessoa = Pessoa()
    pessoa.informar()
    
    print("Seu nome é ", self.no)
    print("Seu e-mail é ", self.em)
    print("Seu numero é ", self.nu)
