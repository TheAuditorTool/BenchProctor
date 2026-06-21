# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest80464():
    raw_body = request.get_data(as_text=True)
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
