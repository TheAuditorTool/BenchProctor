# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import tempfile


def BenchmarkTest05706():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
