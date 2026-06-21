# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import urllib.request


def BenchmarkTest80576():
    multipart_value = request.form.get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', multipart_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = multipart_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
