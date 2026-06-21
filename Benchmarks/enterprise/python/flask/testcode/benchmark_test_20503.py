# SPDX-License-Identifier: Apache-2.0
import random
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest20503():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
