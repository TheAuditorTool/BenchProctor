# SPDX-License-Identifier: Apache-2.0
import yaml
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest12452():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
