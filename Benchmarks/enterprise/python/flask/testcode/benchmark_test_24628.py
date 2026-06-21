# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest24628():
    host_value = request.headers.get('Host', '')
    random.seed(int(host_value) if str(host_value).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
