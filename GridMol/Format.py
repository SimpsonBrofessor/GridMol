
#----------------------------------------#
#----- FORMAT MOL                   -----#
#----- create Mol/SDF text file     -----#
#----------------------------------------#
def Format(atoms, bonds, version):

    atom_lines = []
    for atom in atoms:
        x = str(atom.get_x()).ljust(8)
        y = str(atom.get_y()).ljust(8)
        z = str(atom.get_z()).ljust(8)
        name = atom.get_name().ljust(4)

        atom_line = x
        atom_line += y
        atom_line += z
        atom_line += name
        atom_line += " 0  0  0  0  0  0  0  0  0  0  0  0\n"
        atom_lines.append(atom_line)

    bond_lines = []
    for bond in bonds:
        atom_a = bond.get_atom_a()
        atom_b = bond.get_atom_b()
        bond_type = bond.get_bond_type()

        bond_line = str(atom_a).ljust(4)
        bond_line += str(atom_b).ljust(4)
        bond_line += str(bond_type).ljust(4)
        bond_line += " 0  0  0  0\n"
        bond_lines.append(bond_line)
    

    title = "Output Molecule\n"
    program = "GridMol\n"
    comment = "v" + str(version) + "\n"

    atom_count = str(len(atoms)).ljust(4)
    bond_count = str(len(bonds)).ljust(4)
    stext = "0 0 0 0 0 0 0 0999 V2000\n"

    counts = str(atom_count)
    counts += str(bond_count)
    counts += stext

    mol_lines = title
    mol_lines += program
    mol_lines += comment
    mol_lines += counts
    for line in atom_lines:
        mol_lines += line
    for line in bond_lines:
        mol_lines += line
    mol_lines += "M  END\n"
    return mol_lines
