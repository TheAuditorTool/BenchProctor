# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06795():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
