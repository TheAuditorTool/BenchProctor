# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest16851():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    requests.get(str(data))
    return jsonify({"result": "success"})
