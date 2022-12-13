
set1={23, 42, 65, 57, 78, 83, 29}
set2={57, 83, 29, 67, 73, 43, 48}
print("Intersection:",set1.intersection(set2))
set1=set1.difference(set1.intersection(set2))
print("Set 1 après suppression :",set1)