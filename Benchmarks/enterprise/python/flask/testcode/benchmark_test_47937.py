# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest47937():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})
