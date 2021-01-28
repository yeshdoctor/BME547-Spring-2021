def interface():
    while(True)
        print("Blood Test Analysis")
        response = input('Choose an option (1-HDL, 9-Quit)')
        if response == "1":
            HDLdriver()
        elif response ==  "9":
            return
def HDLdriver():
    HDL = int(input_HDL)
    analysis = analyze_HDl(HDL)
    output_HDL(HDL,analysis)

def analyze_HDl(HDL):
    if HDL >= 60: return "Normal"
    elif 60>HDL>=40: return "Borderline Low"
    else: return "Low"

def output_HDL(HDL,analysis):
    print("The HDL level of {HDL} is {analysis}".format(HDL,analysis))

def input_HDL():
    return(input("Input HDL level:"))