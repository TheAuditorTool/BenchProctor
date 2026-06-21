# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest01497():
    xml_value = request.get_data(as_text=True)
    if auth_check('user', str(xml_value)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
