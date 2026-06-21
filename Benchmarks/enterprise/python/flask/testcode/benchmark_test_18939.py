# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest18939():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    session['data'] = str(data)
    return jsonify({"result": "success"})
