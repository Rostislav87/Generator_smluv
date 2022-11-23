# Zadat možnost vytvoření smlouvy
def print_option():    
    text = print("""
Please select the option number of action you want to perform:
0. salary change
1. job change
2. contract prolongation 
""")
    return text

# Funkce pro nahrání vybrané šablony
def load_template():
    option = int(input(print_option()))

    # Umístění šablon 
    temp0 = "C:\\Users\\rosta\\Python\\Python_kurz\\Lekce 9\\Generator_smluv\\Templates\\salary_change.txt"  
    temp1 = "C:\\Users\\rosta\\Python\\Python_kurz\\Lekce 9\\Generator_smluv\\Templates\\job_change.txt"
    temp2 = "C:\\Users\\rosta\\Python\\Python_kurz\\Lekce 9\\Generator_smluv\\Templates\\contract_prolongation.txt" 
    if option == 0:
        with open(temp0) as template:
            return template.read()
    elif option == 1:
         with open(temp1) as template:
            return template.read()
    else:
        with open(temp2) as template:
            return template.read()        
    
        
# Funkce pro nahrání zaměstnaneckých dat
def load_employees_data():

    # Umístění zaměstnaneckých dat
    employee_data_path = "C:\\Users\\rosta\\Python\\Python_kurz\\Lekce 9\\Generator_smluv\\employees.txt"
    with open (employee_data_path) as employee_file:
        return employee_file.read()

# Umístění pro vygenerované smlouvy
contracts = "C:\\Users\\rosta\\Python\\Python_kurz\\Lekce 9\\Generator_smluv\\Contracts"

load_template()
load_employees_data()

