# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest43216():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
