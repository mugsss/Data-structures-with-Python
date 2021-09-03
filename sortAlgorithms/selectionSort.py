#DSA-Exer-19

def swap(num_list, first_index, second_index):
    #Remove pass and copy the code written earlier for this function
    temp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = temp


def find_next_min(num_list,start_index):
    small = num_list[start_index]
    #print(small)
    position = start_index
    for i in range(start_index,len(num_list)-1):
        k = i+1
        #print(k)
        if(num_list[k]<small):
            small = num_list[k]
            position = k
    return position
   

def selection_sort(num_list):
    for s in range(0,len(num_list)):
        x = find_next_min(num_list,s)
        #print(x)
        swap(num_list,s,x)


#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)


'''

def selSort(list1):
    #print(list1)
    for i in range(0,len(list1)):
        sPo = i
        for j in range(i+1,len(list1)):
            if(list1[sPo] > list1[j]):
                sPo = j
        list1[i],list1[sPo] = list1[sPo],list1[i]
        #print(list1)

    print(list1)


list1 = [9,7,6,5,8]
selSort(list1)

'''

