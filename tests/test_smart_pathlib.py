import os

import pytest
from google.cloud import storage

from smart_pathlib import exists, stat


GCS_TRANSPORT_PARAMS = {
    'client': storage.Client.create_anonymous_client()
}


@pytest.mark.parametrize("uri,expected,transport_params", [
    (os.path.abspath(__file__), True, None),
    ('./file_not_found', False, None),
    ('gs://smart_pathlib_test/test_file.txt', True, GCS_TRANSPORT_PARAMS),
    ('gs://smart_pathlib_test/file_not_found', False, GCS_TRANSPORT_PARAMS),
])
def test_local_file_exists(uri, expected, transport_params):
    assert exists(uri, transport_params=transport_params) == expected


def test_stat():
    path = os.path.abspath(__file__)
    st = stat(path)
    assert isinstance(st, os.stat_result)
    with open(path, 'rb') as f:
        sz = len(f.read())
    assert st.st_size == sz
