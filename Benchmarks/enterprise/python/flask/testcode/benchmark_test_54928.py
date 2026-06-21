# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest54928():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = relay_value(forwarded_ip)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
