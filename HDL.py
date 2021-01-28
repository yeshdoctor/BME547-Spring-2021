def interface():
    while(True):
        print("Blood Test Analysis")
        response = input('Choose an option (1-HDL, 2-LDL, 9-Quit)')
        if response == "1":
            HDLdriver()
        if response == "2":
            LDLdriver()
        elif response ==  "9":
            return
def HDLdriver():
    response = input_HDL()
    HDL = int(response)
    analysis = analyze_HDl(HDL)
    output_HDL(HDL,analysis)

def LDLdriver():
        response = input_LDL()
        LDL = int(response)
        analysis = analyze_LDL(LDL)
        output_LDL(LDL,analysis)

def analyze_HDl(HDL):
    if HDL >= 60: return "Normal"
    elif 60>HDL>=40: return "Borderline Low"
    else: return "Low"

def output_HDL(HDL,analysis):
    print("The HDL level of {H} is {A}".format(H=HDL,A=analysis))

def input_HDL():
    return(input("Input HDL level:"))

def analyze_LDL(LDL):
    if LDL <= 130: return "Normal"
    elif 158>LDL>=130: return "Borderline High"
    else: return "High"

def output_LDL(LDL,analysis):
    print("The LDL level of {L} is {A}".format(L=LDL,A=analysis))

def input_LDL():
    return(input("Input LDL level:"))

interface()
