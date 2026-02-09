import sys
def downcase_it(s):
    return s.lower()

def main():
    params = sys.argv[1:]

    if len(params) == 0:
        print("none")
    else:
        for p in params:
            print(downcase_it(p))
main()