##  Assumptions
this is pretty tough cause im not sure how many readings you've taken, and I don't know the format of your table.\
But this is probably the only free time I'll get so LOL

1. You guys measured the time it took for 2 ml blocks to get poured out (in the manual it was 5ml but you said smthin abt 2 so)

2. You know the height of the water column of every 2 ml block (ha and hb) and you've calculated h = (ha + hb)/2

3. The equation is 1/t = smthin x (h) I'm gonna assume all the values are in CGS so if its not theres gonna be some multiple of 10 difference in the slope. (I hope the time is in second atleast)

## File format
I need a CSV file, which I know you probably dont know, but there, its the thing that I told you yesterday. format should be like this

```
t1,h1
t2,h2
t3,h3
```
> its fine even if you put decimals in this t is in seconds, h in cm


## What does the program do?
takes the t, converts it to $1/t$, plots that on the y axis, plots corresponding $h$ against the x axis, takes a best-fit line for all the points, tells you what the slope is. After you find the slop you can find the value of ${\eta}$.


