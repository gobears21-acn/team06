input = 'A'
try:
    number = int(input)
    print(input)
except ValueError:
    print ('Unexpected parameter')
except:
    print ('Other error')