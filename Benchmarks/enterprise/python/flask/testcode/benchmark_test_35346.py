# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest35346():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
