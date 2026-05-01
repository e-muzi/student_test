# Before start, you should install the library by: pip install peptides

# Task 1: The Protein Identity Card
- Introduction: Every protein has a unique “fingerprint”. To identify a protein in a lab, we often look at its Molecular Weight (how heavy it is) and its Isoelectric Point (pI) (the pH level where the protein has no net electrical charge).

- Your Goal: Write a script named yourname_id_card.py that calculates these two values for the sequence: MAVKVAVNGFGGRIGRLVTRAA.

- Solution Guide:
1.	Library: Use the peptides library.
2.	Steps: 
a) Import the library, 
b) Create a “Peptide” object using the sequence string, 
c) Call the methods for molecular weight and pI, 
d) Use print() to show the results.

# Task 2: The Heat Resistance Index
- Introduction: In this year iGEM, we care about Thermostability. One way to predict if a protein can handle heat is the Aliphatic Index. This is a calculation based on the volume occupied by aliphatic side chains (Alanine, Valine, Isoleucine, and Leucine). Higher volume usually means better heat resistance.

- Your Goal: Compare two sequences in a script called yourname_heat_check.py. Which one is more heat-stable?
•	Protein A: MSSKTTK
•	Protein B: MAVKVAVNGF

- Solution Guide:
1.	Library: Use peptides.
2.	Method: Look for the .aliphatic_index() function in the documentation.
3.	Logic: Calculate the index for both and use an if statement to print which one is higher.
Reference material (take a look how to use the library!):
Peptides.py: https://peptides.readthedocs.io/en/stable/api/peptide.html 


# STEP-BY-STEP NOTE SHEET:
Basic terminal commands (mac set-up, you should have done it in the previous session):
1.	Install homebrew (https://brew.sh/)
2.	Install Git (https://git-scm.com/install/)
3.	‘cd desktop’ (or another folder you like)
4.	‘git clone <link>’ (replace <link> with the GitHub repo HTTPS link sent in group)

After cloning, you can open VS code (or other compiler) and select the folder you just cloned.

Then, open a new folder, and add your ‘.py’ file inside for each task and complete them following the above instructions. 

After completing the tasks:

1. git add the changes

2. type in commit messages, e.g. ‘Task 1 complete’

3.git push (sync changes)
