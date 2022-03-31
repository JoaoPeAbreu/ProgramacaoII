from config import *


class Casa (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formato = db.Column(db.String(254))

    def __str__(self):
        return f'Casa: {self.formato}'


class Quarto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    dimensoes = db.Column(db.String(254))

    casa_id = db.Column(db.Integer, db.ForeignKey(Casa.id),
                        nullable=False)
    casa = db.relationship("Casa")

    def __str__(self):
        s = f'Quarto: {self.nome}, {self.dimensoes}, em: {str(self.casa)}'
        s += f'na casa: {str(self.casa)}'
        return s

class Mobilia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    funcao = db.Column(db.String(254))
    material = db.Column(db.String(254))
    quarto_id = db.Column(db.Integer, db.ForeignKey(Quarto.id),
                        nullable=False)
    quarto = db.relationship("Quarto")
    
    def __str__(self):
        s = f'Nome:  {self.nome}, Função: {self.funcao}, Material: {self.material}'
        if self.quarto_id:
            s += f'No quarto: {str(self.quarto)}'
        return s

if __name__ == "__main__":  # teste das classes

    if os.path.exists(arquivobd):  # se houver o arquivo...
        os.remove(arquivobd)  # ...apagar!

    db.create_all()  # criar tabelas

    print("*** TESTE criando objetos")

    c1 = Casa(formato="Germânica")  # cria uma casa

    # persiste para criar o id
    db.session.add(c1)
    db.session.commit()

    print(c1)  # exibir atributos da casa

    q1 = Quarto(nome="Sala", dimensoes="6x5 metros", casa=c1)
    q2 = Quarto(nome="Banheiro", dimensoes="3x4 metros", casa=c1)

    db.session.add(q1)
    db.session.add(q2)
    db.session.commit()

    print(q1, q2)

    m1 = Mobilia(nome='armario', funcao='guardar coisas', material='madeira', quarto=q1)
    m2 = Mobilia(nome='mesa de canto', funcao='colocar coisas', material='metal', quarto=q2)

    db.session.add(m1)
    db.session.add(m2)
    db.session.commit()

    print(m1, m2)

    print("*** TESTE com todos os dados")
    print(c1)  # casa
    # quartos da casa, sem lista reversa
    for q in db.session.query(Quarto).filter(Quarto.casa_id == c1.id).all():
        print(q)
