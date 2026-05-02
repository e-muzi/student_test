import peptides
peptide = peptides.Peptide("MAVKVAVNGFGGRIGRLVTRAA")
isopt = peptide.isoelectric_point(pKscale="EMBOSS")
weight = peptide.molecular_weight()
print("PI value is:", isopt)
print("Molecule weight is:", weight)
