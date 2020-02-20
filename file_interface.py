def read_file(filename):
    with open(filename, "r") as f:
        content = f.read()
        info = {}
        part1 = content.split("\n")
        part2 = part1[1].split(" ")
        part3 = part1[2:]
        part1 = part1[0].split(" ")
        info['n_books'] = int(part1[0])
        info['n_libreries'] = int(part1[1])
        info['days'] = int(part1[2])
        info['profits'] = [int(elem) for elem in part2]
        print(info)
        flag = True
        libraries = []
        for elem in part3:
            temp = elem.split(' ')
            if temp[0] is '':
                break
            if flag:
                library = {'books':temp[0], 'signup':temp[1], 'ship':temp[2]}
                flag = False
            else:
                library['list'] = temp
                libraries.append(library)
                flag = True
        info['libreries'] = libraries
        return info

def out_file(filename):
    pass