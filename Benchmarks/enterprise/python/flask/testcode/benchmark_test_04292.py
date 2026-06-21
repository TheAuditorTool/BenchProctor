# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest04292():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    requests.get(str(data))
    return jsonify({"result": "success"})
