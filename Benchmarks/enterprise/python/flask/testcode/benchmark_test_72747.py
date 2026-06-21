# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72747():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    exec(str(processed))
    return jsonify({"result": "success"})
