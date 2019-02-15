def bubble_sort(collection):
        length=len(collection)
        for i in range(length-1):
            swapped=False
            for j in range(length-1-i):
                swapped=True
                if collection[j]>collection[j+1]:
                    collection[j],collection[j+1]=collection[j+1],collection[j]
            if not swapped:
                break
        return collection
if __name__=='__main__':
    user_input=input("Please input seperated by a comma:").strip()
    unsorted=[int(item) for item in user_input.split(',')]
    print(*bubble_sort(unsorted),sep=',')
