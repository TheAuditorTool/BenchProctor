# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest31129():
    user_id = request.args.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
