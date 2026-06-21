# SPDX-License-Identifier: Apache-2.0
import os
import json
from flask import request, jsonify


def BenchmarkTest67381():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    os.seteuid(65534)
    return jsonify({"result": "success"})
