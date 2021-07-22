def task(arr,lower,upper):
    '''Return missing range given sorted arr
    given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"]. '99' is present in the output'''
    
    arr.insert(0,lower)
    output_list = []

    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if diff > 1:
            if diff == 2:
                output_list.append(str(arr[i]+1))
            else:
                output_list.append(str(arr[i]+1) + "->" + str(arr[i+1]-1))
    
    #this below condition is outside of for loop because upper will be inclusive in the output, for above given case, 99 is inclusive in output
    if(upper - arr[-1]) <= 1:
        output_list.append(str(upper))
    else:
        output_list.append(str(arr[-1]+1) + "->" + str(upper))

    return output_list

result = task([0, 1, 3, 50, 75],0,99)
print(result)

