#By u/TheRealRumplestomp of Reddit
#An interesting one liner for part 1
with open('input.txt') as fp: print (sum( [ (1 if l[(3*i) % (len(l)-1) ] == '#' else 0) for i,l in enumerate(fp)] ))
