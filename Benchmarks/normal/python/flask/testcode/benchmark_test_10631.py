# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import tempfile


def BenchmarkTest10631():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
