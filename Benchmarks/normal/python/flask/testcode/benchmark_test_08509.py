# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest08509():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
