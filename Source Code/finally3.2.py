

def group(a, b) -> None:
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("This results in infinity")
    else:
        print(c)
    finally:
        print("this part is always executed")


group(2.0, 3.0)
group(3.0, 3.0)
