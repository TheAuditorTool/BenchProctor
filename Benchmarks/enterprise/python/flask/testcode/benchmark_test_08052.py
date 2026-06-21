# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest08052():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
