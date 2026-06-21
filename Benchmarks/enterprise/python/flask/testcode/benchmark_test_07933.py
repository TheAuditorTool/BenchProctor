# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest07933():
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
