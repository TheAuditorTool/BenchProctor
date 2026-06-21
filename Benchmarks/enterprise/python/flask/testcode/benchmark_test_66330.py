# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest66330():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value}'
    session['user'] = str(data)
    return jsonify({"result": "success"})
