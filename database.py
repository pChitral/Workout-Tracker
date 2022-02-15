from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('WorkoutTracker.db')
cursor = connection.cursor()

cursor.execute("INSERT INTO Workout_Subtype VALUES('2','1', 'Shoulder')")
cursor.execute("INSERT INTO Workout_Subtype VALUES('3','1', 'Tricep')")
cursor.execute("INSERT INTO Workout_Subtype VALUES('4','2', 'Back')")
cursor.execute("INSERT INTO Workout_Subtype VALUES('5','2', 'Bicep')")
cursor.execute("INSERT INTO Workout_Subtype VALUES('6','3', 'Legs')")

connection.commit()
