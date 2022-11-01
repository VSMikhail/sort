def count_lines(file):
    with open(file, encoding='utf-8') as f:
        string_list = f.readlines()
    return len(string_list)


def sort_file_by_length(files):
    length_dict = {}
    length_list = []
    for file in files:
        length_dict[str(count_lines(file))] = file
    for key in sorted(length_dict):
        length_list.append(length_dict[key])
    return length_list, length_dict


def merge_files(info):
    for file in info[0]:
        with open(file, encoding='utf-8') as f:
            data = f.read()
        with open('sorted.txt', 'a', encoding='utf-8') as f:
            f.write(info[1][str(count_lines(file))])
            f.write('\n')
            f.write(str(count_lines(file)))
            f.write('\n')
            f.write(data)
            f.write('\n')


files_list = ['1.txt', '2.txt', '3.txt']
merge_files(sort_file_by_length(files_list))
