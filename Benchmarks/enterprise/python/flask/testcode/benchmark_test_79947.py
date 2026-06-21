# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79947():
    xml_value = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(xml_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
