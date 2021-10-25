# read the initial and final quality of atoms
initial_atoms_quality = int(input())
final_atom_quality = int(input())
half_life = 0
half_life_days = 12

while initial_atoms_quality >= final_atom_quality:
    half_life += 1
    initial_atoms_quality /= 2

days = half_life * half_life_days
print(days)
