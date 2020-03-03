# cli program for tracking workouts

import datetime

lines = ["", "", "", "\n"]

start = datetime.datetime.now()

outf = open("workout.txt", 'w')

pushCount = 0
pullCount = 0
squatCount = 0
jackCount = 0
abCount = 0

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
    elif "ab" in exercise:
        abCount += reps
    else:
        print("invalid exercise")
        continue
    
    lines.append(datetime.datetime.now().strftime("[%H:%M:%S] ") + ' '.join(i)+"\n")

end = datetime.datetime.now()
duration = str(end - start)
duration = duration[:duration.rfind('.')]

totalreps = pushCount+pullCount+squatCount+jackCount+abCount
rpm = totalreps/((end-start).total_seconds()/60) # reps per minute
rps = (end-start).total_seconds()/(len(lines)-4) # rest per set

lines[0] = "Start:\t" + start.strftime("%Y-%m-%d %H:%M:%S") + "\n"
lines[1] = "End:\t" + end.strftime("%Y-%m-%d %H:%M:%S") + "\n"
lines[2] = "Duration: " + duration + "\n"

lines.append("\nTotal:\n")
lines.append(str(pushCount) + "\tpushups\n")
lines.append(str(pullCount) + "\tpullups\n")
lines.append(str(squatCount) + "\tsquats\n")
lines.append(str(jackCount) + "\tjumping jacks\n")
lines.append(str(abCount) + "\tab exercises\n")

lines.append("\nStats:\n")
lines.append(str(pushCount+pullCount+squatCount+jackCount) + "\ttotal reps\n")
lines.append(str(int(rpm)) + "\treps per minute\n")
lines.append(str(int(rps)) + "\tseconds between sets on average\n")

for line in lines:
    outf.write(line)

outf.close()