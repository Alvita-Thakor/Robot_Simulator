def get_coordinate(st,min_c,max_c):
    while True:
        c=input(st)
        if c.isnumeric():
            c=int(c)
            if min_c<=c<=max_c :
                return c
            print("Give valid coordinates")
            continue
        print("Coordinates should be numeric")