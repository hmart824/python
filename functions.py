def reverseAnArray (lst):
    i = 0;
    j = len(lst) - 1;
    while(i < j):
        temp = lst[i];
        lst[i] = lst[j];
        lst[j] = temp;
        i = i +1;
        j= j-1;
    print(lst);

def rotateAnArray(lst):
    pass


array = [1,2,3,4,5,6,7];
reverseAnArray(array);