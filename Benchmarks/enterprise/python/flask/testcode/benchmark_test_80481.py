# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest80481():
    xml_value = request.get_data(as_text=True)
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    auth_check('user', data)
    return jsonify({"result": "success"})
