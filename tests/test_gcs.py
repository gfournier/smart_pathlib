import os

from google.cloud import storage

from smart_pathlib.gcs import exists, stat


def test_exists():
    path = 'gs://smart_pathlib_test/test_file.txt'
    assert exists(path, {'client': storage.Client.create_anonymous_client()})
    path = 'gs://smart_pathlib_test/missing_file'
    assert not exists(path,
                      {'client': storage.Client.create_anonymous_client()})


def test_stat():
    path = 'gs://smart_pathlib_test/test_file.txt'
    st = stat(path, {'client': storage.Client.create_anonymous_client()})
    assert isinstance(st, os.stat_result)
    assert st.st_size == os.stat(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'resources',
        'test_file.txt')).st_size
