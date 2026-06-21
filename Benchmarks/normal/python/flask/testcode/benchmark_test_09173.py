# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest09173():
    xml_value = request.get_data(as_text=True)
    auth_check('user', xml_value)
    return jsonify({"result": "success"})
