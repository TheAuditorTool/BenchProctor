# SPDX-License-Identifier: Apache-2.0
import random
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest69848():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
