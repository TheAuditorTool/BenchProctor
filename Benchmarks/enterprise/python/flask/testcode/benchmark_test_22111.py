# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
import tempfile


def BenchmarkTest22111(path_param):
    path_value = path_param
    data = unquote(path_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
