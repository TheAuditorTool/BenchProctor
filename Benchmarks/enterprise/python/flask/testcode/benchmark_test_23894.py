# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23894():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
