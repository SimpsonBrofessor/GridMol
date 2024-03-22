import os
from GridMol.GridMol import Atom

#----------------------------------------#
#----- LOAD                         -----#
#----- parse vina text file         -----#
#----------------------------------------#
def Load(load_directory):
    atoms_loaded = []
    
    try:
        docked_molecules = os.listdir(load_directory)
        for molecule_filename in docked_molecules:
            vina_filename = molecule_filename + '.pdbqt'
            vina_filepath = os.path.join(load_directory, molecule_filename, vina_filename)
            if os.path.isfile(vina_filepath):
                vina_file = open(vina_filepath)
                atoms = parse(vina_file)
                atoms_loaded += atoms
                vina_file.close()

        return atoms_loaded

    except OSError:
        print(f'DOCKED DIRECTORY ERROR: {load_directory}')


def parse(vina_file):
    score_line = None
    atom_lines = []
    atoms = []

    # vina
    lines = vina_file.readlines()
    for line in lines:
        if 'REMARK VINA RESULT:' in line:
            score_line = line
        if 'ATOM' in line:
            atom_lines.append(line)
        if 'ENDMDL' in line:
            break

    #score
    if not score_line: return
    score_parse = score_line.split(' ')
    score_parse = [i for i in score_parse if i != '']
    score = float(score_parse[3])

    # atoms
    for line in atom_lines:
        atom_parse = line.split(' ')
        atom_parse = [i for i in atom_parse if i != '']
        charge_type_parse = atom_parse[11].split('\n')

        name = str(atom_parse[2])
        x = float(atom_parse[5])
        y = float(atom_parse[6])
        z = float(atom_parse[7])
        charge = float(atom_parse[10])
        charge_type = str(charge_type_parse[0])

        # validation
        if name.isnumeric(): continue

        atom = Atom(score, name, x, y, z, charge, charge_type)
        atoms.append(atom)

    return atoms
