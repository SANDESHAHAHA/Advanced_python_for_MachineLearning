# 11. Implement a function to remove duplicates from a list without using set().
unique_list=[]
def remove_duplicates(lst):
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

result=remove_duplicates([1,1,2,3,4,4,5,6,9,6,7,8,9])
print(f"List withotu duplicates: {result}")
   
            
        
    