import itertools
import re

largos = {
    '1H': 2, '2H': 3, '4H': 2, '5H': 2, '7H': 2, '8H': 2, '10H': 3, '11H': 2,
    '1V': 2, '2V': 2, '3V': 3, '4V': 2, '6V': 3, '7V': 2, '8V': 2, '9V': 2,
}

palabras = set(re.sub(r'[^\w] ', '', '''Este es un texto para sacar palabras y asi
emular las claves del diccionario expuesto en el ejercicio.

Artificial Intelligence (AI) is a big field, and this is a big book. We have tried to explore the
full breadth of the field, which encompasses logic, probability, and continuous mathematics;
perception, reasoning, learning, and action; and everything from microelectronic devices to
robotic planetary explorers. The book is also big because we go into some depth.
The subtitle of this book is “A Modern Approach.” The intended meaning of this rather
empty phrase is that we have tried to synthesize what is now known into a common frame-
work, rather than trying to explain each subfield of AI in its own historical context. We
apologize to those whose subfields are, as a result, less recognizable.
''').lower().split())


variables = []
dominios = {}

for var, largo in largos.items():
    # agrego variables
    variables.append(var)

    # optamos por restringir el dominio a solo las palabras que poseen el largo
    # para completar la variable. Otra posibilidad es agregar restricciones.
    dominios[var] = [x for x in palabras if len(x) == largo]
