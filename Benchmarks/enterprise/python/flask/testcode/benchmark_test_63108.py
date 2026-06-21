# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest63108():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    auth_check('user', data)
    return jsonify({"result": "success"})
