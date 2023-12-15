

try:
    file = open('myfile.txt')
    print('File exists')
    print(file.readline())

except FileNotFoundError:
    print('File does not exist')
    
except Exception:
    print('An error occurred')


