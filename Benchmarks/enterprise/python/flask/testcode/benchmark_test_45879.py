# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45879():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})
