

def foo(index_value) -> int:
    try:
        list1 = ['Maths',
                 'Science',
                 'Stats',
                 'Operational Research']
        print(list1[index_value])
        return 1
    except:
        print("Invalid Input")
        return 0

    finally:
        print("this part will be executed always") 

myFavSubject = foo(0)
print("My favourite subject is {}".format(myFavSubject))

