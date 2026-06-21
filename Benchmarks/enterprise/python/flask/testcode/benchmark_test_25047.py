# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest25047():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})
