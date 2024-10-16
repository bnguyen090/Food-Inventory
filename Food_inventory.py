# Formatting of 
# inventory =(
#         ['Potato',['sweet', 9.0], [230,'26D']], 
#         ['Bread', ['bakery','organic','whole wheat',0.5], [ 800, '21C']], 
#         ['Shrimp', ['frozen foods', 'large', 3.0], [75, '51A']], 
#         ['Ice cream',['dairy', 'choclate', 0.25],[215, '9E']],
#         ['Apple', ['fruits', 'non-GMO', 5.0], [1540, '37B']])


def update_inventory(dict1, restock=None):  # Figure out the parameters and add
    # to the function signature
    # Put your function body here
    if restock == None:
        return dict1
    for item in restock:
        for food, val in dict1.items():
            to_update = val
            if food == item[0]: #checks to see if the restock items is already in dict1
    #            print(to_update)
                for n in range(len(item[1])):
                    if item[1][n] != '':
                        to_update[0].insert(-1,item[1][n]) #if so this updates the dict1 item
                to_update[1][0] += item[2][0] #adds to the item  already in dict1
                if item[2][1] != '':
                    to_update[1][1] += ' ' + item[2][1] #adds the last part of the restock 
                    #in the section where the item is
    to_append = []
    
    
    for indice in range(len(restock)):
        if restock[indice][0] not in dict1.keys(): #if the restock item isn't already in dict1
            to_append.append(int(indice))
    for val in to_append:
        to_update = restock[val][1:]
        dict1[restock[val][0]] = to_update #adds the value into dict1, with new key
    #print(to_append)
    return dict1
inventory ={
        'Potato':[['sweet', 9.0], [230,'26D']], 
        'Bread': [['bakery','organic','whole wheat',0.5], [ 800, '21C']], 
        'Shrimp': [['frozen foods', 'large', 3.0], [75, '51A']], 
        'Ice cream':[['dairy', 'choclate', 0.25],[215, '9E']],
        'Apple': [['fruits', 'non-GMO', 5.0], [1540, '37B']]
        }
restock = [['Shrimp', ['farm-raised'], [80, '50A 50B']], ['Bread', [''], [135, '']]]
#print(update_inventory(inventory, restock))


def merge_inventory (inventory_old =[], new={}):  # Figure out the parameters 
    #and add to the function signature
    # Put your function body here
    #not done
    dict1 = {}
    list1 = []
    merged = {}
    if new != '':
        for foods in inventory_old:
            dict1[foods[0]] = foods[1:] # puts inventory_old into a dict
        for keys,values in new.items():
            #print(new[keys])
            list1.append([keys, values[0], values[1]]) #puts new dict into list
        
        merged = update_inventory(dict1, list1) #this alows me to plug it 
        #into update_invetory with teh right parameters
    
    else:
        return inventory_old
    return merged #change to final after
inventory = (['Potato',['sweet', 9.0], [230,'26D']], 
                ['Bread', ['bakery','organic','whole wheat',0.5], [ 800, '21C']], 
                ['Shrimp', ['frozen foods', 'large', 3.0], [75, '51A']], 
                ['Ice cream',['dairy', 'choclate', 0.25],[215, '9E']],
                ['Apple', ['fruits', 'non-GMO', 5.0], [1540, '37B']])
new_inventory =  {'Apple':[['sweet'], [100,'']], 'Bread': [['gluten-free'], [520, '21D']], 'Chicken': [['butchery', 'farm-raised', 4.5], [974, '50A']]}

#print(merge_inventory(inventory, new_inventory))


def products_info (products, product_info, new_products=[]):
    list1 = []
    new_dict = {}
    for i in range(len(products)):
        list1.extend([[products[i],product_info[i][0], product_info[i][1]]])
        #turns product and product info into a list in order to use it in merge_invetory
        if new_products != []:
            if new_products[i] != []:
                new_dict[products[i]] = new_products[i]
                #turns new products into a dict
    final = merge_inventory(list1, new_dict)
    #print(list1, new_dict)
    


    return  final#make sure u outpust a list then dict
products = ('Apple', 'Milk', 'Bread', 'Salmon')
products_detail =([['fruits', 'non-GMO', 5.0], [1540, '37B']], [['dairy','sugar-free', 1.0], [2500, '11A']], [['bakery','organic','whole wheat',0.5], [120, '21C']], [['frozen foods', 'wild cut', 3.0], [456, '6E']])
new_products_detail = ([['sweet'], [100,'']], [], [['gluten-free'], [520, '21D']], [])
#print(products_info(products, products_detail, new_products_detail))

def digits_summation (n):
    # Put your function body here
    sum = 0 
    n = str(n)
    if n != (): #base code
        if len(n) != 0:
            #print(len(n))
            sum += int(n[0]) #adding to sum the value of the first number
            n = n[1:] #removes the first number
        if len(n) != 0:
            sum += digits_summation(int(n)) #recursion case
    
    return sum
#print(digits_summation(12345))

def vowel_counts (some_str, results=None):
    if results == None:
        results = {} #turns into dict
    # Put your function body here
    vowels= 'AEIOUaeiou' #to check if vowels
    if some_str != '': #base case
        if some_str[0] in vowels: 
            if some_str[0] in results:#check if already in dict
                results[some_str[0]] += 1
            else:
                results[some_str[0]] = 1 #if not adds a new one
        some_str = some_str[1:]
        if some_str != '': #recursion case
            vowel_counts(some_str, results)
    return results#use results to store results from first iteration
