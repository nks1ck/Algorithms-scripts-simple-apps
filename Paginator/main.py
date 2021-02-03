def more(text, numlines=10):
    lines = text.splitlines()
    while lines:
        piece = lines[:numlines]
        lines = lines[numlines:]
        for line in piece:
            print(line)

        if lines and input('More?') not in ['y', 'Y']: break


if __name__ == '__main__':
    import sys
    more(open(sys.argv[1]).read(), 10)