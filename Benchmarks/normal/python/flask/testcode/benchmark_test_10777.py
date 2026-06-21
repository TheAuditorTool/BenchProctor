# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest10777():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = coalesce_blank(forwarded_ip)
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    requests.get(str(data))
    return jsonify({"result": "success"})
