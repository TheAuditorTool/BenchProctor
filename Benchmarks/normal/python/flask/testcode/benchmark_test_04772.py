# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04772():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
