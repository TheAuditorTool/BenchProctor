# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest31046():
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
