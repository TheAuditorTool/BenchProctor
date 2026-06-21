# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37646():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
