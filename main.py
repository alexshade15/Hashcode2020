from file_interface import read_file, write_file


def compute_library_score(libs, d, profits, books):
    lib_rank = []
    lib_index = 0
    for lib in libs:
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
        lib_rank.append((lib_index, avail_book_rank, lib_score))
        lib_index += 1

    lib_rank.sort(reverse=True, key=lambda x: x[2])
    return lib_rank[0]


filename = "d_tough_choices"
info = read_file(filename+".txt")
books = set()
for i in range(info['n_books']):
    books.add(i)
days = info['days']
profits = info['profits']
libreries = info['libreries']
output = {}
while days > 0 and len(output) != info['n_libreries']:
    key, value, temp = compute_library_score(libreries, days, profits, books)
    list_books = []
    for elem in value:
        books.remove(elem[0])
        list_books.append(elem[0])
    output[key] = list_books
    print(len(output))
    days -= libreries[key]['signup']

outdict = {}
outdict['n_libreries'] = len(output)
outdict['libreries'] = output
write_file(filename+"_out.txt", outdict)
