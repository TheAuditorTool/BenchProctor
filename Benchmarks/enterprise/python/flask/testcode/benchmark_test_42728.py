# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest42728():
    referer_value = request.headers.get('Referer', '')
    data = to_text(referer_value)
    auth_check('user', data)
    return jsonify({"result": "success"})
