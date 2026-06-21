# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02672():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
