# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


def BenchmarkTest14233():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    yaml.safe_load(data)
    return jsonify({"result": "success"})
