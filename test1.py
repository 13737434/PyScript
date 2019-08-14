def getString(filename):
    with open(filename, "r") as f:
        str=f.read()
    return str

if __name__ == '__main__':
    str=getString("")
    print("")

