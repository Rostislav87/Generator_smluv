# Funkce main
def main():
    # Výběr pro novou smlouvu
    option = int(input(print_option()))
    # Zaměstnanecné data
    employee_file = load_employees_data()
    
    if option == 0:
        temp_file = load_template_salary()
    elif option == 1:
        temp_file = load_template_job_change()
    else:
        temp_file = load_contract_prolongation()
    # Genertování nových smluv        
    for employee_id, employee in employee_file.items():
        print(f"Creating contract for {employee_id} ...")
        write_file(temp_file, employee)
    return print(f"Contract have been succesfully generated.")

# Zadat možnost vytvoření smlouvy
def print_option():    
    print("Please select the option number of action you want to perform:\n0. salary change\n1. job change\n2. contract prolongation")
    return ""

# Funkce pro nahrání vybrané šablony
def load_template_salary():
    # Umístění šablony
    temp0 = "C:\\Users\\rosta\\Python\\Python_kurz\\Lekce 9\\Generator_smluv\\Templates\\salary_change.txt"
    with open(temp0) as template:
        temp_salary = template.read()
    return temp_salary


def load_template_job_change():    
    # Umístění souboru
    temp1 = "C:\\Users\\rosta\\Python\\Python_kurz\\Lekce 9\\Generator_smluv\\Templates\\job_change.txt"
    with open(temp1) as template:
        temp_job_change = template.read()
    return temp_job_change


def load_contract_prolongation():
    # Umístění souboru
    temp2 = "C:\\Users\\rosta\\Python\\Python_kurz\\Lekce 9\\Generator_smluv\\Templates\\contract_prolongation.txt" 
    with open(temp2) as template:
        temp_contract_prolongation = template.read()
    return temp_contract_prolongation


# Funkce pro nahrání zaměstnaneckých dat
def load_employees_data():

    # Umístění zaměstnaneckých dat
    employee_data_path = "C:\\Users\\rosta\\Python\\Python_kurz\\Lekce 9\\Generator_smluv\\employees.txt"
    with open(employee_data_path) as employee_file:
        file = employee_file.read()
    return eval(file)


# Funkce pro zápis hodnot
def write_file(temp_file, employee):

    # Umístění pro vygenerované smlouvy
    filename = f"{employee['full_name']}_contract.txt"
    contracts = f"C:\\Users\\rosta\\Python\\Python_kurz\\Lekce 9\\Generator_smluv\\Contracts"
    with open(f"{contracts}\\{filename}", mode="w") as new_file:
         new_file.write(temp_file.format_map(employee))
    

main()