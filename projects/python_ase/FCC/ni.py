from ase.build import bulk
from ase.io import write

ni = bulk("Ni", crystalstructure="fcc", a=3.52)
ni_conv = bulk(
    "Ni",
    crystalstructure="fcc",
    a=3.52,
    cubic=True
)
ni_super = ni_conv.repeat((3, 3, 3))

print("=" * 60)
print("FCC NICKEL")
print("=" * 60)

print(f"Formula: {ni.get_chemical_formula()}")
print(f"Number of atoms: {len(ni)}")

print("\nCell vectors (Å):")
print(ni.cell)

print("\nCell lengths (Å):")
print(ni.cell.lengths())

print("\nCell angles (deg):")
print(ni.cell.angles())

print("\nVolume (Å³):")
print(ni.get_volume())

print("\nPeriodic Boundary Conditions:")
print(ni.pbc)

print("\nAtomic positions (Å):")
for atom in ni:
    print(
        f"Atom {atom.index}: "
        f"{atom.symbol} "
        f"{atom.position}"
    )

# Save structure
write("fcc_ni.cif", ni)
write("fcc_ni.xyz", ni)
write("fcc_ni_supercell.cif", ni_super)
