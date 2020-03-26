import numpy as np

og = np.array([[0,0,1,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,1],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,1,0,1,1,0,0,0],[0,0,0,1,1,0,0,0]])

filterr = np.random.rand(3,3)


def main():

    finalRes = SliceToFilter(og,filterr)
    print( finalRes)
    while len(finalRes) >= len(filterr):
        finalRes = SliceToFilter( finalRes,filterr)
        print(finalRes)


def SliceToFilter(og,filterr):
    
    result = np.zeros((len(og)-2,len(og[0])-2))
    for row in range(len(result)):
        for colm in range(len(result[0])):
            cut = og[row:row+3,colm:colm+3]*filterr
            num = ConvertToDotNum(cut)
            result[row][colm] += num
    return result



def ConvertToDotNum(arr):
    
    sum1 = 0
    for row in range(len(arr)):
        for colm in range(len(arr[0])):
            sum1 += arr[row,colm]
    return sum1



if __name__ == "__main__":

    main()