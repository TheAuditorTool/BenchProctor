# SPDX-License-Identifier: Apache-2.0
import yaml
import base64
from flask import request, jsonify


def BenchmarkTest14621():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
