# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78113():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
