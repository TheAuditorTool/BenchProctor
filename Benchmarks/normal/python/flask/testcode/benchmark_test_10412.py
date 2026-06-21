# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest10412():
    cookie_value = request.cookies.get('session_token', '')
    yaml.safe_load(cookie_value)
    return jsonify({"result": "success"})
