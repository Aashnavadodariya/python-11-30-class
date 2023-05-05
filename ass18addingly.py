s="abc"
if len(s) > 2:
    if s.endswith('ing'):
        s+='ly'
    else:
        s+='ing'
print(s)
