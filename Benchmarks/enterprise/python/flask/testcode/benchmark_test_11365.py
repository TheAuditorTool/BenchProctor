# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import tempfile


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest11365():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
