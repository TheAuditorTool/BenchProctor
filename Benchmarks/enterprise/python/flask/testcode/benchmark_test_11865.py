# SPDX-License-Identifier: Apache-2.0
import os
import json
from flask import request, jsonify


def BenchmarkTest11865():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
