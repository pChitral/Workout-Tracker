import datetime as dt
print(dt.datetime.today())
workout_dictionary = {}
if(dt.datetime.today()):
    workout_dictionary['date'] = dt.datetime.today()
    workout = workout_data = {}
    todaysWorkout = input('what are you going to do? \n')

    if(todaysWorkout == 'push'):

        print('Start with incline db press')
        for i in range(3):
            set = i
            reps = input(f'How many reps did you complete for set {i +1} \n')
            print(reps)
