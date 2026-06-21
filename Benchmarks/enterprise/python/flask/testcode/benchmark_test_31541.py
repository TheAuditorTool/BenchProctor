# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import pickle


def BenchmarkTest31541():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
