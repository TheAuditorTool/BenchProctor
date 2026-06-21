# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest32332():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
