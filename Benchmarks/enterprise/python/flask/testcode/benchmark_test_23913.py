# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import tempfile


def BenchmarkTest23913(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
