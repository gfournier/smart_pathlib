import os

from smart_pathlib.local_file import exists, stat


def test_exists():
    path = os.path.abspath(__file__)
    assert exists(path, None)
    path = os.path.abspath(__file__) + '.tmp'
    assert not exists(path, None)


def test_stat():
    path = os.path.abspath(__file__)
    st = stat(path, None)
    assert isinstance(st, os.stat_result)
    with open(path, 'rb') as f:
        sz = len(f.read())
    assert st.st_size == sz
