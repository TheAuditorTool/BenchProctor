# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest17784():
    header_value = request.headers.get('X-Custom-Header', '')
    data = normalise_input(header_value)
    if not re.fullmatch('^[\\w\\s.{}\\[\\]:_$\'\\"|=-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return jsonify({"result": "success"})
