# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest49523():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    session['data'] = str(data)
    return jsonify({"result": "success"})
