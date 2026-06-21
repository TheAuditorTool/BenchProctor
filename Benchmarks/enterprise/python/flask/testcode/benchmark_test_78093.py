# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest78093():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % str(forwarded_ip)
    session['data'] = str(data)
    return jsonify({"result": "success"})
