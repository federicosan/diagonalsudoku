values= {'A1':'23','B1':'23','G3':'23','A5':'12345','A8':'23'}
naked_twins = [ (x,z) for x in values.keys() for z in values.keys() if ((x!=z) and (values[x] == values[z]) and (len(values[x])==2) and (x[0]==z[0] or x[1]==z[1]))]
print(naked_twins)
