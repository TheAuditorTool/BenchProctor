# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import tempfile


def BenchmarkTest11002(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
