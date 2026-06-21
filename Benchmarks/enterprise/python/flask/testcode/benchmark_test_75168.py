# SPDX-License-Identifier: Apache-2.0
import tempfile
from flask import jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest75168(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
