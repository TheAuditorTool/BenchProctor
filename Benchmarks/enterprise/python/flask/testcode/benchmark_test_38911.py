# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest38911():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    session['data'] = str(processed)
    return jsonify({"result": "success"})
