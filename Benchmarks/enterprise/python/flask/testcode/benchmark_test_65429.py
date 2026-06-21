# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
import unicodedata


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest65429(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}
