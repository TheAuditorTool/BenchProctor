# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
import tempfile


def BenchmarkTest32593(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
