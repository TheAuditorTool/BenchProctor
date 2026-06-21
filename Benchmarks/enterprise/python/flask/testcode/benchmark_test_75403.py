# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75403():
    raw_body = request.get_data(as_text=True)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(raw_body))
    return jsonify({"result": "success"})
