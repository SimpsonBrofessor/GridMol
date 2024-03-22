
#----------------------------------------#
#----- CELL                         -----#
#----- cubic component of grid      -----#
#----------------------------------------#
class Cell():

    def __init__(self, cell_x, cell_y, cell_z):
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.cell_z = cell_z
        self.atom_list = []

    def insert_atom(self, atom):
        self.atom_list.append(atom)

    def get_list(self):
        return self.atom_list
    
    def get_selected(self):
        return self.atom_selected

    def get_x(self):
        return self.cell_x
    
    def get_y(self):
        return self.cell_y
    
    def get_z(self):
        return self.cell_z