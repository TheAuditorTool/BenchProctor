# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest08115():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    json.loads(data)
    return jsonify({"result": "success"})
