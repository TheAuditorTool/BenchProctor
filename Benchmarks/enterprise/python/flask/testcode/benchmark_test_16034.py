# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest16034():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    requests.get(str(data))
    return jsonify({"result": "success"})
