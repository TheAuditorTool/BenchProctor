# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest62772():
    xml_value = request.get_data(as_text=True)
    data = normalise_input(xml_value)
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
