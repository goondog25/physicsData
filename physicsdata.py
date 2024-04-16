import sqlite3

class Particle:
    def __init__(self, name, amuMass, charge):
        self.name = name
        self.amuMass = amuMass
        self.charge = charge
        
class Proton(Particle):
    def __init__(self):
        super().__init__("Proton", 1.007276, 1)

class Neutron(Particle):
    def __init__(self):
        super().__init__("Neutron", 1.008665, 0)

class Electron(Particle):
    def __init__(self):
        super().__init__("Electron", 0.00054858, -1)

class Atom:
    def __init__(self, protons, neutrons, electrons):
        self.protons = protons
        self.neutrons = neutrons
        self.electrons = electrons
        self.conversion_factor = 1.6726219e-27

    def calculate_amu_mass(self):
        amu_mass = (self.protons * 1.007276) + (self.neutrons * 1.008665)
        return amu_mass
    
    def calculate_kg_mass(self):
        amu_mass = self.calculate_amu_mass()
        kg_mass = amu_mass * self.conversion_factor
        return kg_mass
    
    def calculate_charge(self):
        net_charge = self.protons + (self.electrons * -1)
        return net_charge
    
    def add_protons(self, moreProtons):
        self.protons += moreProtons

    def remove_protons(self, lessProtons):
        self.protons -= lessProtons

    def add_neutrons(self, moreNeutrons):
        self.neutrons += moreNeutrons

    def remove_neutrons(self, lessNeutrons):
        self.neutrons -= lessNeutrons

    def add_electrons(self, moreElectrons):
        self.electrons += moreElectrons
    
    def remove_electrons(self, lessElectrons):
        self.electrons -= lessElectrons

