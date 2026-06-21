# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest07402():
    xml_value = request.get_data(as_text=True)
    data = relay_value(xml_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    session['data'] = str(processed)
    return jsonify({"result": "success"})
