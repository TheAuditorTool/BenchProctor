# SPDX-License-Identifier: Apache-2.0
import os
import json
from flask import request, jsonify


def BenchmarkTest03452():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
