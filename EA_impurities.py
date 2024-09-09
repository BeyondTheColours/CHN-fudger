import os

solvents = {
	"toluene" : [7, 8, 0, 92.141],
	"THF" : [4, 8, 0, 72.11],
	"hexane" : [6, 14, 0, 86.178],
	"pentane" : [5, 12, 0, 72.151]
}

c = 49
h = 58
n = 2
mr = 801.60

os.system('clear')

retry = True
print_message = False

while retry:
	print("Select solvent impurity to include:")
	count = 1
	for key in solvents:
		print(f"{key}")

	if print_message:
		print("Enter one of the available solvent choices (or None)")
		print("(this is case sensitive)")

	try:
		choice = input("--> ")
		
		acc = False
		for key in solvents:
			acc = acc or (choice == key)
		
		if acc:
			retry = False
			
		else:
			print_message = True
			os.system('clear')
	
	except ValueError:
		print_message = True
		os.system('clear')

os.system('clear')
print_message = False
retry = True
while retry:

	if print_message:
		print("Enter a demical number only")
		print(f"(\'{solv_equiv}\' was entered)")
	else:
		pass

	try:
		print("Enter the number of equivalents of solvent per molecule of compound")
		solv_equiv = input("--> ")
		solv_equiv = float(solv_equiv)
		retry = False

	except ValueError:
		print_message = True
		os.system('clear')

def calc_chn(c, h, n, mr):
	p_c = round(100*(c*12.011)/mr, 2)
	p_h = round(100*(h*1.008)/mr, 2)
	p_n = round(100*(n*14.007)/mr, 2)
	
	return [p_c, p_h, p_n]

out_no_solvent = calc_chn(c, h, n, mr)
print(f"CHN no solvent   : C : {out_no_solvent[0]}, H : {out_no_solvent[1]}, N : {out_no_solvent[2]}\n")

solvent_data = solvents[choice]

c = c+(solv_equiv*solvent_data[0])
h = h+(solv_equiv*solvent_data[1])
n = n+(solv_equiv*solvent_data[2])
mr = mr+(solv_equiv*solvent_data[3])


out_with_solvent = calc_chn(c, h, n, mr)
print(f"CHN with solvent : C : {out_with_solvent[0]}, H : {out_with_solvent[1]}, N : {out_with_solvent[2]}\n")
