from gendiff import reader


def differ(file1: dict, file2: dict):
    same = []
    diff1 = []
    diff2 = []

    for key1 in file1:
        for key2 in file2:
            if key1 == key2 and file1[key1] == file2[key2]:
                same.append(f'{key1}: {file1[key1]}')
            elif key1 == key2 and file1[key1] != file2[key2]:
                diff1.append(f'{key1}: {file1[key1]}')
                diff2.append(f'{key2}: {file2[key2]}')
            elif key1 not in [i for i in file2]:
                diff1.append(f'{key1}: {file1[key1]}')
            elif key2 not in [i for i in file1]:
                diff2.append(f'{key2}: {file2[key2]}')

    return list(set(same)), list(set(diff1)), list(set(diff2))


def formatter(diff):
    same = ['    ' + i.lower() + '\n' for i in diff[0]]
    diff1 = ['  - ' + i.lower() + '\n' for i in diff[1]]
    diff2 = ['  + ' + i.lower() + '\n' for i in diff[2]]
    sorting = same + diff1 + diff2
    sorting.sort(key=lambda x: x[4])
    output = ''.join(sorting)
    return '{\n' + output + '}\n'


def generate_diff(file_path1, file_path2):
    file1 = reader.read(file_path1)
    file2 = reader.read(file_path2)
    diff = differ(file1, file2)
    return formatter(diff)
