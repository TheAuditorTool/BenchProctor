# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest07372():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
