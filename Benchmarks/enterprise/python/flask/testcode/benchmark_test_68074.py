# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest68074():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
