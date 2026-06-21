# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest79127():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
