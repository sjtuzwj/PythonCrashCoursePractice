import pygal
from die import Die

die_1=Die(6)
die_2=Die(10)
times=50000

results=[]
for roll_num in range(times):
    result=die_1.roll()+die_2.roll()
    results.append(result)


frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

hist=pygal.Bar()

cp="D"+str(die_1.num_sides)+"+D"+str(die_2.num_sides)
hist.title="Results of rolling "+cp+ " "+str(times)+" times"
hist.x_labels=[str(x) for x in range(2,max_result+1)]
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add(cp,frequencies)
hist.render_to_file('die_visual.svg')