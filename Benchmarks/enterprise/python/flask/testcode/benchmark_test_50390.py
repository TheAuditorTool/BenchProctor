# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50390():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % (json_value,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
