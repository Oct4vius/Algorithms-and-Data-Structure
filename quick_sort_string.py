import random

"""
Time complexity 
best case O(n log n)
worst case O(n↑2)
"""

def quick_sort(values):
    if len(values) <= 1:
        return values
    
    lees_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            lees_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quick_sort(lees_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


names = ["Francina Vigneault", "Lucie Hansman", "Nancie Rubalcaba", "Elida Sleight", "Guy Lashbaugh", "Ginger Schlossman", "Suellen Luaces", "Jamey Kirchgesler", "Amiee Elwer", "Lacresha Peet", "Leonia Goretti", "Carina Bunge", "Renee Brendeland", "Andrew Mcgibney", "Gina Degon", "Deandra Pihl", "Desmond Steindorf", "Magda Growney", "Tawana Srivastava", "Tammi Todman", "Harley Mussell", "Iola Bordenet", "Edwardo Khela", "Myles Deanne", "Elden Dohrman", "Ira Hooghkirk", "Eileen Stigers", "Mariann Melena", "Maryrose Badura", "Ardelia Koffler", "Lacresha Kempker", "Charlyn Singley", "Lekisha Tawney", "Christena Botras", "Mike Blanchet", "Cathryn Hinkson", "Errol Shinkle", "Mavis Bhardwaj", "Sung Filipi", "Keiko Dedeke", "Lorelei Morrical", "Jimmie Lessin", "Adrianne Hercules", "Latrisha Haen", "Denny Friedeck", "Emmett Whitesell", "Sina Sauby", "Melony Engwer", "Alina Reichel", "Rosamond Shawe", "Elinore Benyard", "Sang Bouy", "Ed Aparo", "Sheri Wedding", "Sang Snellgrove", "Shaquana Sones", "Elvia Motamed", "Candice Lucey", "Sibyl Froeschle", "Ray Spratling", "Cody Mandeville", "Donita Cheatham", "Darren Later", "Johnnie Stivanson", "Enola Kohli", "Leann Muccia", "Carey Philps", "Suellen Tohonnie", "Evelynn Delucia", "Luz Kliment", "Lettie Jirjis", "Francene Klebe", "Margart Scholz", "Sarah Growden", "Glennis Gines", "Rachael Ojima", "Teofila Stample", "Narcisa Shanley", "Gene Lesnick", "Malena Applebaum", "Norma Tingey", "Marianela Mcmullen", "Rosalva Dosreis", "Dallas Heinzmann", "Sade Streitnatter", "Lea Pelzel", "Judith Zwahlen", "Hope Vacarro", "Annette Ayudan", "Irvin Cyree", "Scottie Levenstein", "Agustina Kobel", "Kira Moala", "Fawn Englar", "Jamal Gillians", "Karen Lauterborn", "Kit Karratti", "Steven Deras", "Mary Rosenberger", "Alonso Viviano"]

sorted_names = quick_sort(names)

for n in sorted_names:
    print(n)