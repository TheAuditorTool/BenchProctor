# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest05112():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
