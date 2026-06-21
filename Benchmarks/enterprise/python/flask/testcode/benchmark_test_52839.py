# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest52839():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
