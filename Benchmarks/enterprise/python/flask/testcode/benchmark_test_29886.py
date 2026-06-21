# SPDX-License-Identifier: Apache-2.0
import random
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest29886(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
