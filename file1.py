def bubble_sort(list):
    sorted_lst=list[:]
    is_sorted=False
    while is_sorted==False:
        swaps=0
        for i in range(len(list)-1):
            if sorted_lst[i]>sorted_lst[i+1]: # swap
                temp=sorted_lst[i]
                sorted_lst[i]=sorted_lst[i+1]
                sorted_lst[i+1]=temp
                swaps+=1
        print(swaps)
        if swaps==0:
            is_sorted=True
    return sorted_lst


print(bubble_sort([2, 1, 5, 4, 7, 6, 10, 34, 15]))
