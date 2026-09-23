import sys

if len(sys.argv) - 1 < 2:
    print("none")
else:
    params = sys.argv[1:]
    params.reverse()
    for param in params:
        print(param)