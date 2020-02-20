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
        flag = True
        libraries = []
        for elem in part3:
            temp = elem.split(' ')
            if temp[0] is '':
                break
            if flag:
                library = {'books':int(temp[0]), 'signup':int(temp[1]), 'ship':int(temp[2])}
                flag = False
            else:
                library['list'] = [int(x) for x in temp]
                libraries.append(library)
                flag = True
        info['libreries'] = libraries
        return info


def write_file(filename, output):
    with open(filename, 'w') as f:
        f.write(str(output['n_libreries'])+"\n")
        for key, value in output['libreries'].items():
            f.write(str(key)+" "+str(len(value))+"\n")
            i = 0
            for elem in value:
                f.write(str(elem))
                if i == len(value)-1:
                    f.write("\n")
                    break
                else:
                    f.write(" ")
                i += 1

