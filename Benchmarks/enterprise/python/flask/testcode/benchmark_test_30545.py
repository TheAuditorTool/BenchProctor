# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest30545():
    xml_value = request.get_data(as_text=True)
    data = default_blank(xml_value)
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
