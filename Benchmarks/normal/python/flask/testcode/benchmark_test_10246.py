# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10246():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
