# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest13431():
    ua_value = request.headers.get('User-Agent', '')
    data = ensure_str(ua_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
