# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest48578():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
