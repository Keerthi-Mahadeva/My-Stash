"""
Reading data from a list and to write the data into
a CSV file

Data:


[("John Aalberg", 31, "Cross Country Skiing"),
 ("Minna Maarit Aalto", 30, "Sailing"),
 ("Win Valdemar Aaltonen", 54, "Art Competitions"),
 ("Wakako Abe", 18, "Cycling"),
]

"""


data_list = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling"),
            ]

with open("Olympics_details.csv", "w") as olympics_file:
    header_row = "Name, Age, Event"
    olympics_file.write(header_row + "\n") # Write header row to file

    for row in data_list:
        name, age, event = row # Unpacking
        age = str(age) # Converting int to str

        row_tuple = (name, age, event) # making a tuple from string variables
        combined_row = ",".join(row_tuple) # joining the elements of the tuple with a ',' to form a continuous string.
        olympics_file.write((combined_row) + "\n")
