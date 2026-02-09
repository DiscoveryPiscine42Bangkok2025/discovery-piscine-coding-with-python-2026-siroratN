import sys
if len(sys.argv) > 2:
    for p in sys.argv[::-1]:
        print(p)
else:
    print("none")