# SPDX-License-Identifier: Apache-2.0
import random
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest72969():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return jsonify({'token': str(token)}), 200
