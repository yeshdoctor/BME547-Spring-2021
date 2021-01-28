def interface():
	print("Blood Test Analysis")
	while True:
		print("\nOptions")
		print("9 - Quit")
		choice = input("Enter an option:")
		if choice == "9":
			return

def check_HDL(val):
	if val > 60 : return "Normal"
	elif val > 40 : return "Borlerline Low"
	else: return "Low"

def output(x):
	print(x)

def HDL_driver():
	in = input("Enter the HDL")
	output(check_HDL(in))


check_HDL()
