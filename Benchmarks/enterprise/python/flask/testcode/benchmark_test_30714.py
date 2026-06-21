# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest30714():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
