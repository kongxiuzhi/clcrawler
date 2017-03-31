

for i in range(10):
    try:
        print(i)
        raise NameError("ceshi ec")
    except NameError as e:
        print(e)
    


