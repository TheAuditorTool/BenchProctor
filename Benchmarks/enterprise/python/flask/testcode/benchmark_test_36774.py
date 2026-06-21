# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def BenchmarkTest36774():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
