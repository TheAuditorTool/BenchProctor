# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import tempfile


def BenchmarkTest16017(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
