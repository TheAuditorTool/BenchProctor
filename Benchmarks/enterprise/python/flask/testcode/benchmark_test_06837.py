# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest06837():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
