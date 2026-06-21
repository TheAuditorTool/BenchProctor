# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22400():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
