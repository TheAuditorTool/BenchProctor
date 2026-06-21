# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest43111():
    user_id = request.args.get('id', '')
    random.seed(int(user_id) if str(user_id).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
