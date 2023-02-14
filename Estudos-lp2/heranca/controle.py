class ControleBonificacao():
    def __init__(self, total=0):
        self._total = total

    def registra(self, funcionario):
        try:
            self._total += funcionario.get_bonifica()
        except AttributeError:
            print('Deixe de ser gaiato, você não é funcionário')
    @property
    def total(self):
        return  self._total
