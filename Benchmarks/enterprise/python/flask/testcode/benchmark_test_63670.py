# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
import tempfile


def BenchmarkTest63670(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})
