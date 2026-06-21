# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest02647():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})
