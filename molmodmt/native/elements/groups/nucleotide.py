from molmodmt.native.elements import Group

class Nucleotide(Group):

    def __init__(self, id=None, index=None, name=None, type=None):

        super().__init__(id=id, index=index, name=name, type=type)

        self.lettercode = None
