import os
from Setup import Config, Database, Log
from Database import Database as AtomDatabase
from GridMol import Grid, GridMol, Atom, Format, Load, Export


if __name__ == '__main__':

    #----------------------------------------#
    #----- CONFIG                       -----#
    #----------------------------------------#
    config = Config('Config.yml')
    score_threshold = config['Score_Threshold']
    grid_size = config['Grid_Size']
    origin_xyz = {
        'X': config['Receptor']['Origin']['X'],
        'Y': config['Receptor']['Origin']['Y'],
        'Z': config['Receptor']['Origin']['Z']
    }
    box_xyz = {
        'X': config['Receptor']['Box_Size']['X'],
        'Y': config['Receptor']['Box_Size']['Y'],
        'Z': config['Receptor']['Box_Size']['Z']
    }


    #----------------------------------------#
    #----- STARTUP LOG MESSAGE          -----#
    #----------------------------------------#
    Log(config['Version'])


    #----------------------------------------#
    #----- DATABASE OF DOCKED ATOMS     -----#
    #----------------------------------------#
    database_session = Database(config['Database_Directory'], config['Database_Create'])
    atom_database = AtomDatabase(database_session)
    if config['Database_Create']:
        load_directory = os.path.join(os.getcwd(), config['Docked_Directory'])
        atoms_loaded = Load(load_directory)
        atom_database.insert_atoms(atoms_loaded)
    db_atoms = atom_database.get_all_atoms()
    # interface db to GridMol - convert SQL obj to Atom obj
    atom_list = []
    for db_atom in db_atoms:
        score = db_atom.score
        name = db_atom.name
        x = db_atom.x
        y = db_atom.y
        z = db_atom.z
        charge = db_atom.charge
        charge_type = db_atom.charge_type
        atom = Atom(score, name, x, y, z, charge, charge_type)
        atom_list.append(atom)


    #----------------------------------------#
    #----- GRID - 3D CONTAINER OF ATOMS -----#
    #----------------------------------------#
    grid = Grid(grid_size, origin_xyz, box_xyz)
    for atom in atom_list:
        grid.insert_atom(atom) 
    

    #----------------------------------------#
    #----- GRIDMOL - CREATE NEW MOLECULE ----#
    #----------------------------------------#
    grid_list = grid.get_list()
    gen_mol = GridMol(grid_list, score_threshold)
    atoms, bonds = gen_mol.generate_molecule()


    #----------------------------------------#
    #----- SAVE NEW MOLECULE - MOL FILE -----#
    #----------------------------------------#
    output_directory = os.path.join(os.getcwd(), config['Output_Directory'])
    new_molecule = Format(atoms, bonds, config['Version'])
    Export(new_molecule, output_directory)
