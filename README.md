# Number of cord intersections inside Circle
Programming Language: Python

This program calculates the number of intersections among a set of cords inside a circle. It takes a list as an input, where list has two tuple elemnts. The first tuple has radian angle of the cord’s endpoints on the circle, and the second tuple has cord identifier.

Example input : [(0.78, 1.47, 1.77, 3.92), ("s_1", "s_2", "e_1", "e_2")]

The code works as follows:
*  It defines a function get_intersections that takes the input list as a parameter and returns the output integer.

*  It creates an empty dictionary chords that will store the chord identifiers as keys and the sorted radian angles as values. For example, for the previous input, chords will be {1: [0.78, 1.77], 2: [1.47, 3.92]}.

*  It loops through the input list using zip to pair the radian angles and the identifiers. For each pair, it extracts the chord number using re.findall and checks if it is already in chords. If yes, it appends the radian angle to the existing list and sorts it. If no, it creates a new list with the radian angle and assigns it to the chord number.

*  It initializes a variable num_intrsc to zero that will keep track of the number of intersections.
It converts the values of chords to a list called chord_list. For example, for the previous input, chord_list will be [[0.78, 1.77], [1.47, 3.92]].

* It loops through all possible pairs of chords using combinations from itertools. For each pair, it assigns the start and end angles of the first chord to s_1 and e_1, and the start and end angles of the second chord to s_2 and e_2.

* It checks if the chords intersect using the exclusive or (^) operator. The condition is true if one of the endpoints of the second chord is between the endpoints of the first chord, and the other endpoint of the second chord is outside the endpoints of the first chord. For example, for the pair [[0.78, 1.77], [1.47, 3.92]], the condition is true because 1.47 is between 0.78 and 1.77, and 3.92 is outside 0.78 and 1.77.

* If the condition is true, it increments num_intrsc by one.

*  It returns num_intrsc as the output.

*  It prompts the user to enter the input using input and converts it to a Python object using ast.literal_eval.

*  It calls the function get_intersections with the input value and assigns the result to no_of_intersections.

*  It prints the output using print and formatted string.

The program has a time complexity of O(n^2), where n is the number of elements in either first or the second tuple in the list.


