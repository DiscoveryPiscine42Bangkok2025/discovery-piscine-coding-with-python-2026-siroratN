import sys
if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    result_array = list(range(start, end + 1))
    print(result_array)