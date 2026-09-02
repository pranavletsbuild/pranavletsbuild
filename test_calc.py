from calc import square
n=int

def main():
    test_square()

def test_square():
    if square(n)!=n*n:
        print(f"{n} square  was not {n*n}")
   
if __name__=="__main__":                    
    main()
    
