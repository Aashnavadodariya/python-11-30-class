s="a boy is not in poor"
l1=0
l2=0
if "not" in s:
    l1=s.index("not")
    if "poor" in s:
        l2=s.index("poor")
if l2-l1==4:
    s.replace("not poor","good")
