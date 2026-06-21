# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59569():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
