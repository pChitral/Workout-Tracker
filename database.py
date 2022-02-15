from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('WorkoutTracker.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE EXERCISE(Exercise_ID INTEGER, Name TEXT, Workout_Subtype_ID INTEGER)')
connection.commit()