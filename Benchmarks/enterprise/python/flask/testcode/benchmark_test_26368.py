# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import request, jsonify
import os


def BenchmarkTest26368():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
