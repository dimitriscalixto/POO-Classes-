class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        print(f'{self.nome} está filmando')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')

        print(f'{self.nome} está fotografando')
        self.filmando = True


c1 = Camera('canon')
c2 = Camera('Sony')
c1.filmar()
c1.fotografar()
