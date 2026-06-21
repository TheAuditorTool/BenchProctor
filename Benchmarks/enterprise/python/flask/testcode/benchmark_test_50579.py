# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest50579():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
