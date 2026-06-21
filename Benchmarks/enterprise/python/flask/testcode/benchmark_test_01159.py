# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01159():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})
