from pathlib import Path
from gendiff.differ import generate_diff


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name


def test_generate_diff():
    file_path1 = get_path('file1.json')
    file_path2 = get_path('file2.json')
    result_filepath = get_path('result_json')
    assert generate_diff(file_path1, file_path2) == open(result_filepath).read()
