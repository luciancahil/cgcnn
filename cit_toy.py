from ase import Atoms
from ase.io import write

# Example Atoms object (replace with your own)
atoms = Atoms('H2O', positions=[[0, 0, 0], [0.76, 0.58, 0], [-0.76, 0.58, 0]])

# Write to a CIF file
atoms.set_cell([10, 10, 10])
atoms.set_pbc([True, True, True])
write('output.cif', atoms, format='cif')