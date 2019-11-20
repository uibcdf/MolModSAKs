from molmodmt.native.elements import Molecule

class Water(Molecule):

    def __init__(self, index=None, id=None, name=None):

        super().__init__(index=index, id=id, name=name, type="water")

