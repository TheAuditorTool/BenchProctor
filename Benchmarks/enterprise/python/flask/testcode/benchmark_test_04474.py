# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest04474():
    ua_value = request.headers.get('User-Agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
