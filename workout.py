outf = open("workout.txt", 'w')

pushCount = 0
pullCount = 0
squatCount = 0
jackCount = 0

while True:
    i = input("Enter an exercise and rep range: ").split()
    if i[0] == "exit":
        break
    exercise = ' '.join(i[1:])
    reps = int(i[0])

    if "push" in exercise:
        pushCount += reps
    elif "pull" in exercise:
        pullCount += reps
    elif "squat" in exercise:
        squatCount += reps
    elif "jack" in exercise:
        jackCount += reps
    else:
        print("invalid exercise")
        continue
    
    outf.write(' '.join(i)+"\n")

outf.write("\nTotal:\n")
outf.write(str(pushCount) + " pushups\n")
outf.write(str(pullCount) + " pullups\n")
outf.write(str(squatCount) + " squats\n")
outf.write(str(jackCount) + " jumping jacks\n\n")

outf.close()