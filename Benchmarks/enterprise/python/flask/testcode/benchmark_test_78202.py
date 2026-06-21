# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def BenchmarkTest78202():
    user_id = request.args.get('id', '')
    random.seed(int(user_id) if str(user_id).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
