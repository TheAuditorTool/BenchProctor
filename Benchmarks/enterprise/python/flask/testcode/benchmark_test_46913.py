# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
from app_runtime import auth_check


def BenchmarkTest46913():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
