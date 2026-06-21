# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11817():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
