# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest21174():
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
