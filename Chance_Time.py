import random
#import plotly.express as px
import plotly.figure_factory as ff

count = []
diceResults = []
for i in range(0,10):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    diceResults.append(dice_1+dice_2)
    count.append(i)
print(diceResults)

#fig = px.bar(x = diceResults, color = diceResults ,y= count)
fig = ff.create_distplot([diceResults], ["result"])

fig.show()