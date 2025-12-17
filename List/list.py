# List methods
# 1. Add list element (1 element) .append()
my_list = [1, 2 ,3, 4]
my_list.append(5) # ==> my_list = [1,2,3,4,5]

# 2. Add element .extend()
list1 = [2,3,4,5]
list2 = ['a','b']
list1.extend(list2)  # ==> list1 + list2

# 3. sort list .sort() / sorted()
list = [3,5,1,4,9]
list.sort() # ==> [1,3,4,5,9]
# list.sort(reversed = True)  ==> [9,5,4,3,1]
new_list = sorted(list) # list is remained, new_list has sorted

# 4. reversed list
list = [3,5,1,4,9]
list.reverse()  # ==> [9,5,4,3,1]
new_list = list[::-1] # ==> String reversed method (start:stop:step)

# 5. insert element .insert(index, value)
list = [3,5,1,4,9]
list.index(1, 'a')  # ==> [3,'a',5,1,4,9]

# 6. delete element del / .remove(del)
list1 = [2,3,4,5]
del list[1]  # ==> [2,4,5]
del list[:2]  # ==> [4,5]

# 7. Return the first index of the element .index() (no error)
list1 = [2,3,4,5]
index = list1.index(5)  # ==> To check if 5 is in the list

# 8. pop(index) remove the last element
list1 = [2,3,4,5]
ele = list1.pop(5)
# [2,3,4], the number 5 is take out of the list and assigned into ele variable