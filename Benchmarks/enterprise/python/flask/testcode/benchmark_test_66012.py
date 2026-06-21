# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest66012():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value}'
    auth_check('user', data)
    return jsonify({"result": "success"})
