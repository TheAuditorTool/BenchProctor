# SPDX-License-Identifier: Apache-2.0
import yaml
import base64
from flask import request, jsonify


def BenchmarkTest05762():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
