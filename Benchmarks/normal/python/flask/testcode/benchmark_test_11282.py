# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest11282():
    cookie_value = request.cookies.get('session_token', '')
    yaml.load(cookie_value, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
