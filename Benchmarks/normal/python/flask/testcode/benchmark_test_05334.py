# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest05334():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
