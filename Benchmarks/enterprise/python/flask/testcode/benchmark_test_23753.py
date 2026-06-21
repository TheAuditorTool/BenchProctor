# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest23753():
    user_id = request.args.get('id', '')
    data = default_blank(user_id)
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
