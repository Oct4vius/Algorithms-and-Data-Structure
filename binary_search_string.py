names =['Adrianne Hercules', 'Agustina Kobel', 'Alina Reichel', 'Alonso Viviano', 'Amiee Elwer', 'Andrew Mcgibney', 'Annette Ayudan', 'Ardelia Koffler', 'Candice Lucey', 'Carey Philps', 'Carina Bunge', 'Cathryn Hinkson', 'Charlyn Singley', 'Christena Botras', 'Cody Mandeville', 'Dallas Heinzmann', 'Darren Later', 'Deandra Pihl', 'Denny Friedeck', 'Desmond Steindorf', 'Donita Cheatham', 'Ed Aparo', 'Edwardo Khela', 'Eileen Stigers', 'Elden Dohrman', 'Elida Sleight', 'Elinore Benyard', 'Elvia Motamed', 'Emmett Whitesell', 'Enola Kohli', 'Errol Shinkle', 'Evelynn Delucia', 'Fawn Englar', 'Francene Klebe', 'Francina Vigneault', 'Gene Lesnick', 'Gina Degon', 'Ginger Schlossman', 'Glennis Gines', 'Guy Lashbaugh', 'Harley Mussell', 'Hope Vacarro', 'Iola Bordenet', 'Ira Hooghkirk', 'Irvin Cyree', 'Jamal Gillians', 'Jamey Kirchgesler', 'Jimmie Lessin', 'Johnnie Stivanson', 'Judith Zwahlen', 'Karen Lauterborn', 'Keiko Dedeke', 'Kira Moala', 'Kit Karratti', 'Lacresha Kempker', 'Lacresha Peet', 'Latrisha Haen', 'Lea Pelzel', 'Leann Muccia', 'Lekisha Tawney', 'Leonia Goretti', 'Lettie Jirjis', 'Lorelei Morrical', 'Lucie Hansman', 'Luz Kliment', 'Magda Growney', 'Malena Applebaum', 'Margart Scholz', 'Marianela Mcmullen', 'Mariann Melena', 'Mary Rosenberger', 'Maryrose Badura', 'Mavis Bhardwaj', 'Melony Engwer', 'Mike Blanchet', 'Myles Deanne', 'Nancie Rubalcaba', 'Narcisa Shanley', 'Norma Tingey', 'Rachael Ojima', 'Ray Spratling', 'Renee Brendeland', 'Rosalva Dosreis', 'Rosamond Shawe', 'Sade Streitnatter', 'Sang Bouy', 'Sang Snellgrove', 'Sarah Growden', 'Scottie Levenstein', 'Shaquana Sones', 'Sheri Wedding', 'Sibyl Froeschle', 'Sina Sauby', 'Steven Deras', 'Suellen Luaces', 'Suellen Tohonnie', 'Sung Filipi', 'Tammi Todman', 'Tawana Srivastava', 'Teofila Stample']

search_names = ["Latrisha Haen", "Irvin Cyree", "Myles Deanne"]

def binary_search(collection, target):
    first = 0
    last = len(collection) -1
    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] == target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

for n in search_names:
    index = binary_search(names, n)
    print(index, n)