 # Exercise Tracker
    #### Video Demo:  <URL HERE>
    #### Description:

   _Exercise Tracker_
   The Exercise Tracker is a simple Python command-line program that allows users to manage and track their exercises. Users can add new exercises, modify existing ones, and view a list of their defined exercises. The program uses a CSV file (exercises.csv) to store exercise data.

   **Features:**

   *Add Exercise:*
   Users can add a new exercise by providing the exercise name, weight, repetitions, and sets.
   The program checks if the exercise already exists before adding it.
   In addition, the input is checked for correctness so that the wrong data type is not written to the CSV

   *Change Exercise:*
   Users can modify the details of an existing exercise by entering its name.
   They have the option to update the exercise's weight, repetitions, and sets or delete the exercise.

   *See Exercises:*
   Displays a table of all defined exercises, including their name, weight, repetitions, and sets.
   This output in the console was embellished using the "prettytable" library.
   
   **Actions:**
   Users can choose from a set of actions:

   1: Add an exercise
   2: Change an existing exercise
   3: View all exercises
   0: Stop the program
   
   *Usage:*

   Adding an Exercise:
   Choose action 1 and follow the prompts to enter exercise details.
   
   Changing an Exercise:
   Choose action 2, enter the name of the exercise to modify, and follow the prompts.
   
   Viewing Exercises:
   Choose action 3 to display a table of all defined exercises.
   
   Exiting the Program:
   Choose action 0 to stop the program.


   **Design decisions:**

   Of course, a CSV file does not replace a real database. By using MongoDB, for example, the data could have been changed, deleted or searched for much more efficiently. However, as the CSV library was part of the course, I limited myself to it. I also refrained from implementing a class to create the exercises, as this would have made the program unnecessarily complicated (I tried it out). 
   I also made the program stop for 0.5 seconds after executing an action so that the user can see more easily whether something has worked or not