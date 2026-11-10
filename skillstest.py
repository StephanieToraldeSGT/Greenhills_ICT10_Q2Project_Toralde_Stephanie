# i dont get it
from pyscript import display, document

def collect_nonmetal(e):
    
    
    symbolof_element = [ 'H','He','C','N', 'O', 'F', 'Ne','P', 'S', 'Cl','Ar', 'Se', 'Br', 'Kr', 'I', 'Xe', 'R',]

# conversion of symbolof_element, cuz apparently it popped out into the world as a str list
    convertedso_e = tuple(symbolof_element)
    convertedso_e = document.getElementById('elementfinder').value

    element_name = ["Hydrogen", "Helium", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Selenium", "Bromine", "Krypton", "Iodine", "Xenon", "Radon"]

# conversion of element_name, cuz apparently it popped out into the world as a str list
    convertede_n = tuple(element_name)

    symbolelement_elementname = dict(zip(convertedso_e, convertede_n))
    symbolelement_elementname = {
       'H': 'Hydrogen',
       'He' :  'Helium', 
       'C' : 'Carbon',
       'N' : 'Nitrogen',
       'O' : 'Oxygen',
       'F' : 'Fluorine',
       'Ne' : 'Neon',
       'P' : 'Phosphorus',
       'S' : 'Sulfur',
       'Cl' : 'Chlorine',
       'Ar' : 'Argon',
       'Se' : 'Selenium',
       'Br' : 'Bromine',
       'Kr' : 'Krypton',
       'I' : 'Iodine',
       'Xe' : 'Xenon',
       'R' : 'Radon',
    } 

    atomic_no = [ '1', '2', '6', '7', '8', '9', '10', '15', '16', '17', '18', '34', '35', '36', '53', '54', '86']
    
    atomicmass = ['1.008', '4.0026', '12.011', '14.007', '15.999', '18.998', '20.180', '30.974', '32.06', '35.45', '39.948', '78.971', '79.904', '83.798', '126.9045', '131.293', '~222 (no stable mass; mass number)']

    # conversion
    converteda_n = tuple(atomic_no)
    convertedam = tuple(atomicmass)

    # create a dict jic for further use
    atomicno_mass = dict(zip(converteda_n, convertedam))
    atomicno_mass = {
    '1' : '1.008',
    '2'  : '4.0026',
    '6' : '12.011',
    '7' : '14.007',
    '8' : '15.999',
    '9' : '18.998',
    '10' : '20.180',
    '15' : '30.974',
    '16' : '32.06',
    '17' : '35.45',
    '18' : '39.948',
    '34' : '78.971',
    '35' : '79.904',
    '36' : '83.798',
    '53' : '126.9045',
    '54' : '131.293',
    '86' : '~222 (no stable mass; mass number)'
    }

    #combination
    elementatomiccombo = {**symbolelement_elementname, **atomicno_mass}

    display(f' | Symbol: {convertedso_e} | Element Name: {symbolelement_elementname.get(convertedso_e)} | Atomic Number: {elementatomiccombo.get(convertedam)} | Atomic Mass: {elementatomiccombo.get(converteda_n)}', target='output')

# display(f'Ang Ingles ng {english_dictionary['defenestration']} ay {english_dictionary.get('ihagis sa bintana', 'defenestration')}', target='output')

# Hydrogen, Carbon, Nitrogen, Oxygen, Phosphorus, Sulfur, Selenium, Fluorine, Chlorine, Bromine, Iodine, Helium, Neon, Argon, Krypton, Xenon, and Radon.
