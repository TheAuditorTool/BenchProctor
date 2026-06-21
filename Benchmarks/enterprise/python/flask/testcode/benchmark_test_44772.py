# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def BenchmarkTest44772():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
