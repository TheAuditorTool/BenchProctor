# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06892():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
