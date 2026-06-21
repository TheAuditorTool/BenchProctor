# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61939():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
