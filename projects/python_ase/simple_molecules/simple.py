from ase.build import molecule
from ase.io import write

def print_atoms(atoms):
    print("#" * 50)
    print(f"Chemical Formula: {atoms.get_chemical_formula()}")
    print(f"Number of Atoms: {len(atoms)}")
    print(f"Symbols: {atoms.get_chemical_symbols()}")

    print("\nAtomic Positions (Å):")
    for atom in atoms:
        print(
            f"{atom.index:2d}  {atom.symbol:2s}  "
            f"{atom.position[0]:8.4f}  "
            f"{atom.position[1]:8.4f}  "
            f"{atom.position[2]:8.4f}"
        )

    print("\nCenter of Mass:")
    print(atoms.get_center_of_mass())

    print("\nDistance Matrix (Å):")
    print(atoms.get_all_distances())

    print("#" * 50)

h2o = molecule("H2O")
co2 = molecule("CO2")

print("WATER")
print_atoms(h2o)

print("\n\nCARBON DIOXIDE")
print_atoms(co2)

write("h2o.xyz", h2o)
write("co2.xyz", co2)

