# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import urllib.request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest49554():
    multipart_value = request.form.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return jsonify({"result": "success"})
