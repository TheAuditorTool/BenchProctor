# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import urllib.request


def BenchmarkTest33040():
    user_id = request.args.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', user_id):
        return jsonify({'error': 'forbidden'}), 400
    processed = user_id
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
