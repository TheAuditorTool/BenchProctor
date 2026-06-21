# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest70874():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    requests.get(str(data))
    return jsonify({"result": "success"})
