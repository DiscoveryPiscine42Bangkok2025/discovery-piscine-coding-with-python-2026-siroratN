import sys

if len(sys.argv) != 2:
    print('none')
else:
    input_string = sys.argv[1]
    result = ""
    for char in input_string:
        if char == 'z':
            result += 'z'
    if result == "":
        print("none")
    else:
        print(result)