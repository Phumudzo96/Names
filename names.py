names = input("Enter names of learners: ")      # Ask the user to enter the names of thr learner

learners_num = 0

while names != "stop":                          # This is will coutinue asking for the names until stop is typed
    print(names)
    learners_num += 1                           # Count the number of names that are inserte
    names = input("Enter names of learners: ")
            
else:
    print("That all of the learners")
    print(f"There are {learners_num} learners in this class")

