
#Create list nd tuple
eids=[10,102,103,104]
uids=(101,102,104,108)

 
#update-List

eids[2]="John"      
print(eids)         #[10, 102, 'John', 104]

#mutable--Possible to update


#update--Tuple
uids[2]="John"      #TypeError: 'tuple' object does not support item assignment
print(uids)

#Immutable--Not Possible to update


