from file_interface import read_file, write_file
from multiprocessing import Pool



def compute_single_score(lib, d, profits, books, lib_index):
    book_rank = []
    for book in lib['list']:
        if book in books:
            score = profits[book]
            book_rank.append((book, score))

    book_rank.sort(reverse=True, key=lambda x: x[1])
    n_books = lib['ship'] * (d - lib['signup'])
    avail_book_rank = book_rank[:n_books]

    lib_score = 0
    for b in avail_book_rank:
        lib_score += b[1]

    return lib_index, avail_book_rank, lib_score


def compute_library_score(libs, d, profits, books):
    lib_rank = []
    lib_index = 0

    for lib in libs:
        single_lib_score = compute_single_score(lib, d, profits, books, lib_index)
        lib_rank.append(single_lib_score)
        lib_index += 1

    # pool = Pool(None)
    # jobs = []
    #
    # for lib in libs:
    #     jobs.append(pool.apply_async(compute_single_score, (lib, d, profits, books, lib_index)))
    #     lib_index += 1
    # for job in jobs:
    #     single_lib_score = job.get(timeout=None)
    #     print(single_lib_score[0])
    #     lib_rank.append(single_lib_score)

    lib_rank.sort(reverse=True, key=lambda x: x[2]-lib['signup'])
    return lib_rank[0]


filename = "f_libraries_of_the_world"
info = read_file(filename+".txt")
books = set()
for i in range(info['n_books']):
    books.add(i)
days = info['days']
profits = info['profits']
libreries = info['libreries']
output = {}
sum = 0
while days > 0 and len(output) != info['n_libreries']:
    key, value, temp = compute_library_score(libreries, days, profits, books)
    list_books = []
    sum += temp
    if temp > 0:
        for elem in value:
            books.remove(elem[0])
            list_books.append(elem[0])
        output[key] = list_books
        print(len(output), sum)
        days -= libreries[key]['signup']
    else:
        break

outdict = {}
outdict['n_libreries'] = len(output)
outdict['libreries'] = output
write_file(filename+"_out.txt", outdict)
