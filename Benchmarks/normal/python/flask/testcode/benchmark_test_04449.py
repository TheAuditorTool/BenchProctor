# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest04449():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
