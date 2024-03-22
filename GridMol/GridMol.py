from .Atom import Atom
from .Bond import Bond
from .Cell import Cell

#----------------------------------------#
#----- GRID MOL                     -----#
#---- create molecule from 3D grid ------#
#----------------------------------------#
class GridMol():

    def __init__(self, grid_list, score_threshold):
        # apply threshold to each cell from grid
        # create new grid of cells with selected atom
        self.score_threshold = float(score_threshold)
        self.cell_list = []
        for grid_cell in grid_list:
            cell_x = grid_cell.get_x()
            cell_y = grid_cell.get_y()
            cell_z = grid_cell.get_z()
            cell = Cell(cell_x, cell_y, cell_z)
            
            atom_list = grid_cell.get_list()
            atom_list.sort(key=lambda atom: float(atom.get_score()))
            if len(atom_list):
                selected_atom = atom_list[0]
                score = float(selected_atom.get_score())
                if score <= self.score_threshold:
                    cell.insert_atom(selected_atom)
                    self.cell_list.append(cell)


    def create_atoms(self):
        # select grid cells containing atoms
        # convert atom coord to grid coord
        atoms = []
        for cell in self.cell_list:
            x = cell.get_x()
            y = cell.get_y()
            z = cell.get_z()
            atom_list = cell.get_list()
            if len(atom_list):
                atom = atom_list[0]
                score = atom.get_score()
                name = atom.get_name()
                charge = atom.get_charge()
                charge_type = atom.get_charge_type()
                atoms.append(Atom(score, name, x, y, z, charge, charge_type))
        
        return atoms
            
    
    def create_bonds(self):
        bonds = []
        # new_bond = Bond(atom_a, atom_b, bond_type)
        return bonds
    # :) code here 
    # use self.cell_list to iterate through cells 
    # recursive graph theory/branch/tree algorithm to find 'parent chain'... longest chain
    # create Bond obj -> new_bond = Bond(atom_1, atom_2, bond_type)
    # atom_a, atom_b -> index of cells containing indicated atoms for bonding (technically bonding two cells together within the grid... cells contain atoms)
    # bond_type -> 1 = single, 2 = double, 3 = triple



    def generate_molecule(self):
        atoms = self.create_atoms()
        bonds = self.create_bonds()
        return atoms, bonds
