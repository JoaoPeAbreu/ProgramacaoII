class Nota:

    def __init__(self, nota1:int, nota2:int, nota3:int):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def caucular_media(self, media:int):
        self.media = (self.nota1 + self.nota2 + nota3)/3
    
    def __repr__(self):
        s = self.media

if __name__=="__main__":
    N = Nota(nota1=8, nota2=6, nota3=9)
    N.caucular_media()
    N.__repr__()
