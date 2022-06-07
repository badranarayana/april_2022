import sys


def add(a, b):
    return a + b


if __name__ == '__main__':
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

    except Exception:
        print("Got some exception")
        sys.exit()

    out = add(a, b)
    print(out)
