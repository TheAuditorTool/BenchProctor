# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14509():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
