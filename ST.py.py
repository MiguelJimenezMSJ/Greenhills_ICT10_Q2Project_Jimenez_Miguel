from pyscript import display, document

#contains all elements, element symbols, atmoic numbers, and atomic mass
Non_metals = {
    'H': ['Hydrogen', 1, 1.008],
    'C': ['Carbon', 6, 12.011],
    'N': ['Nitrogen', 7, 14.007],
    'O': ['Oxygen', 8, 15.999],
    'P': ['Phosphorus', 15, 30.974],
    'S': ['Sulfur', 16, 32.06],
    'F': ['Fluorine', 9, 18.998],
    'Cl': ['Chlorine', 17, 35.45],
    'Se': ['Selenium', 34, 78.97],
    'Br': ['Bromine', 35, 79.90],
    'I': ['Iodine', 53, 126.90],
    'He': ['Helium', 2, 4.0026],
    'Ne': ['Neon', 10,  20.180],
    'Ar': ['Argon', 18, 39.948],
    'Kr': ['Krypton ', 36, 83.798],
    'Xe': ['Xenon ', 54, 131.293],
    'Rn': ['Radon', 86, 222]
}

#where all the data is compiled and shows the results
def search_element(e):
    E_symbol = document.getElementById('Symbol').value.strip().capitalize()

    E_name = Non_metals.get(E_symbol,['Does not exist in the non-metals list.', 'N/A', 'N/A'])

    document.getElementById('result').innerHTML = ''

    display('Element Information:', target='result')
    display(f'Element Symbol: {E_symbol}', target='result')
    display(f'Element Name: {E_name[0]}', target='result')
    display(f'Atomic Number: {E_name[1]}', target='result')
    display(f'Atomic Mass: {E_name[2]}', target='result')