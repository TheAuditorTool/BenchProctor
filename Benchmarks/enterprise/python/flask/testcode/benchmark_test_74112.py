# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest74112():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    session['user'] = str(data)
    return jsonify({"result": "success"})
