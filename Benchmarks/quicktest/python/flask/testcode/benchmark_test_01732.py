# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def BenchmarkTest01732():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
