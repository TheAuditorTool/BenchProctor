# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def BenchmarkTest31354():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = forwarded_ip if forwarded_ip else 'default'
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
