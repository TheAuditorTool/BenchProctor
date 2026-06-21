# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01212():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
