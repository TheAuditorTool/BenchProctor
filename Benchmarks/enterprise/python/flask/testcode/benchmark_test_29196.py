# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest29196():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
