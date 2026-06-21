# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
import tempfile


def BenchmarkTest55831(path_param):
    path_value = path_param
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(path_value))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
