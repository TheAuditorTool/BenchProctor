# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest00481():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
