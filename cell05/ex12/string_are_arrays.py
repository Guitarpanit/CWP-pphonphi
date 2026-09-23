import sys

if len(sys.argv) - 1 != 1:
    print("none")
else:
    text = sys.argv[1]
    count = text.count("z")
    if count == 0:
        print("none")
    else:
        print("z" * count)