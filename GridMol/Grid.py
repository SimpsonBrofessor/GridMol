from .Cell import Cell

#----------------------------------------#
#----- GRID                         -----#
#----- 3D array of cells            -----#
#----------------------------------------#
class Grid():

    def __init__(self, grid_size, origin_xyz, box_xyz):
        self.grid_size = float(grid_size)
        self.origin_x = float(origin_xyz['X'])
        self.origin_y = float(origin_xyz['Y'])
        self.origin_z = float(origin_xyz['Z'])
        self.box_x = float(box_xyz['X'])
        self.box_y = float(box_xyz['Y'])
        self.box_z = float(box_xyz['Z'])
        # create empty grid of cells
        self.cell_list = []
        self.count_x = int(self.box_x / self.grid_size)
        self.count_y = int(self.box_y / self.grid_size)
        self.count_z = int(self.box_z / self.grid_size)
        for z in range(self.count_z):
            for y in range(self.count_y):
                for x in range(self.count_x):
                    cell = Cell(x, y, z)
                    self.cell_list.append(cell)
        

    def insert_atom(self, atom):
        # distance from origin
        distance_x = float(atom.x - self.origin_x)
        distance_y = float(atom.y - self.origin_y)
        distance_z = float(atom.z - self.origin_z)
        # grid position
        cell_x = int(distance_x / self.grid_size)
        cell_y = int(distance_y / self.grid_size)
        cell_z = int(distance_z / self.grid_size)
        # cell index
        cell_index_z = cell_z * (self.count_x * self.count_y)
        cell_index_y = cell_y * self.count_x
        cell_index = cell_x + cell_index_y + cell_index_z
        
        cell = self.cell_list[cell_index]
        cell.insert_atom(atom)

    
    def get_list(self):
        return self.cell_list

