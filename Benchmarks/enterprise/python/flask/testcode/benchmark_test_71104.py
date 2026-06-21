# SPDX-License-Identifier: Apache-2.0
import random
import os
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest71104():
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
