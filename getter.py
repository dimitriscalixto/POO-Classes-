class Connection:

    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self):
        # setter
