# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00619():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
