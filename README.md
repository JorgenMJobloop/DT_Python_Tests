# DT_Python_Tests
Unittest for learning material in Python3

# Kjøre filene
    - rediger koden i funksjoner.py
    - Kjør filen main.py

# Steg 1
    - Åpne filen funksjoner.py og les hva som står i python docstringen
    implementer denne logikken.
```py
# Nedenfor er en docstring, den forklarer hva funksjonen skal returnere
"""
Example function that return the argument string given 
concatinated with the message "from an example string"

Parameters
----------
string : str
    The parameter variable 

Returns
-------
str
    string + "from an example string"

"""
def example_function(string: str):
    return string + " from an example string"

print_example = example_function("Hello") # -> Hello from an example string

```

# Steg 2
    - Les hva testene ønsker å få returnert i linjen som sier "self.assertEqual()" foreløpig er det ikke viktig å forstå helt hva self og assertEqual gjør, det er noe vi kommer til senere. MEN, selve test_funksjoner.py filen skal ikke endres, bare funksjoner.py.

# Steg 3
    - Oppfyll kravene i testene og les eventuelle feilmeldinger som kan oppstå.
    - Last opp ditt eget repository og lever på vanlig måte.

Lykke til!
