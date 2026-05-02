import peptides
peptide_no = 2
peptide_list = []
peptide_list.append(peptides.Peptide("MSSKTTK"))
peptide_list.append(peptides.Peptide("MAVKVAVNGF"))
highest = 0
highest_no = 0
for i in range(0,len(peptide_list)):
  alic_index = peptide_list[i].aliphatic_index()
  if alic_index > highest:
    highest = alic_index
    highest_no = i + 1
print("The",highest_no, "st/nd/rd/th peptide has the best heat resistence index")
print("Which is", peptide_list[highest_no-1])
#it seems like i've done many negative improvements to the program yay! Let's go time complexity as i hv to loop once~