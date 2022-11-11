class Particle:
   def __init__(self, name, charge):
       self.name = name
       self.charge = charge

   def show_particle(self):
       print(f'The particle {self.name} has a charge of {self.charge}')


p = Particle("Muon", "-1")

p.show_particle()