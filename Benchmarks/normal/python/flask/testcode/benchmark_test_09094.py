# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json


def BenchmarkTest09094():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
