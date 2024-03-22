from Database.Tables import Atom as AtomTable

#----------------------------------------#
#----- DATABASE                     -----#
#---- SQLite for storing atom data ------#
#----------------------------------------#
class Database():
    
    def __init__(self, database):
        self.database = database

    def get_all_atoms(self):
        session = self.database()
        atom_list = session.query(AtomTable).all()
        return atom_list
    
    def insert_atoms(self, atom_list):
        session = self.database()

        for atom in atom_list:
            entry = AtomTable()
            entry.score = atom.get_score()
            entry.name = atom.get_name()
            entry.x = atom.get_x()
            entry.y = atom.get_y()
            entry.z = atom.get_z()
            entry.charge = atom.get_charge()
            entry.charge_type = atom.get_charge_type()
            session.add(entry)
            session.commit()
