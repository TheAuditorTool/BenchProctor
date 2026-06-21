# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import tempfile


def BenchmarkTest55763():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
