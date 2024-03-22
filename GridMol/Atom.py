
#----------------------------------------#
#----- ATOM                         -----#
#----- component of docked molecule -----#
#----------------------------------------#
class Atom():

    def __init__(self, score, name, x, y, z, charge, charge_type):
        self.score = score
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.charge = charge
        self.charge_type = charge_type

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z
    
    def get_charge(self):
        return self.charge
    
    def get_charge_type(self):
        return self.charge_type