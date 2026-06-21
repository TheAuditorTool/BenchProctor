# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest71624():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    requests.get(str(data))
    return jsonify({"result": "success"})
