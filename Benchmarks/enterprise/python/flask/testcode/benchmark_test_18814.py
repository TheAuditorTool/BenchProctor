# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import urllib.request


def BenchmarkTest18814():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
