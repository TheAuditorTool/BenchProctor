# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest53870():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
