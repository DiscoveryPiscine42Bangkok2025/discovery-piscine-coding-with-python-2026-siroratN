import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    needed_z = 8 - len(s)
    print(s + ('Z' * needed_z))

def main():
    params = sys.argv[1:]
    
    if len(params) < 1:
        print("none")
        return

    for p in params:
        length = len(p)
        
        if length > 8:
            shrink(p)
        elif length < 8:
            enlarge(p)
        else:
            print(p)

main()