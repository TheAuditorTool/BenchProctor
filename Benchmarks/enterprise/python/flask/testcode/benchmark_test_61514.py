# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61514():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % str(json_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
