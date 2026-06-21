# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest34908():
    raw_body = request.get_data(as_text=True)
    data = normalise_input(raw_body)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
