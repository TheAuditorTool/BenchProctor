# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest78052():
    xml_value = request.get_data(as_text=True)
    data = relay_value(xml_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    session.clear()
    session['user'] = str(data)
    return jsonify({"result": "success"})
