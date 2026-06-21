# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21957():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(json_value))
    return jsonify({"result": "success"})
