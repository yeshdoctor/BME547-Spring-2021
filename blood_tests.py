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




interface()
