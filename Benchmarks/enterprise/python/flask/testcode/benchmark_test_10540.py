# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest10540():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    requests.get(str(data))
    return jsonify({"result": "success"})
