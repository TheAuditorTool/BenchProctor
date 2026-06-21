# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest45504():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    session['data'] = str(forwarded_ip)
    return jsonify({"result": "success"})
