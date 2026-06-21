# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def BenchmarkTest11319():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
