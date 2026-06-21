# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest09511():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
