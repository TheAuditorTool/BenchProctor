# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def BenchmarkTest65758():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(json_value))
    return jsonify({"result": "success"})
