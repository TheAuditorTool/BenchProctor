# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest30515():
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
