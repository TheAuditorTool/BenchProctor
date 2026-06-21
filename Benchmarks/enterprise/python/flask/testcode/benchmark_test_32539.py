# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32539():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
