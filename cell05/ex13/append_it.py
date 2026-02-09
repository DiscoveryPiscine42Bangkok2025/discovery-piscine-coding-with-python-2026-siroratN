import sys

param = sys.argv[1:]

if not param:
    print("none")
else:
    for i in param:
        if not i.endswith("ism"):
            print(i + "ism")