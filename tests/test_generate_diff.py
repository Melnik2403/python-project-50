from gendiff.differ import generate_diff, differ


def test_generate_diff():
    result = ('{\n- follow: false\n'
              '  host: hexlet.io\n'
              '- proxy: 123.234.53.22\n'
              '- timeout: 50\n'
              '+ timeout: 20\n'
              '+ verbose: true\n}')

    assert generate_diff('/home/ivan/python-project-50/tests/file1.json',
                         '/home/ivan/python-project-50/tests/file2.json') == result
