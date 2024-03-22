
#----------------------------------------#
#----- BOND                         -----#
#----- connection between two atoms -----#
#----------------------------------------#
class Bond():
    # bond type: single = 1, double = 2, triple = 3

    def __init__(self, atom_a, atom_b, bond_type=1):
        self.atom_a = atom_a
        self.atom_b = atom_b
        self.bond_type 

    def get_atom_a(self):
        return self.atom_a
    
    def get_atom_b(self):
        return self.atom_b
    
    def get_bond_type(self):
        return self.bond_type