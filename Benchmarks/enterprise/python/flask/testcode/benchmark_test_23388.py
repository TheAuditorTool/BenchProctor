# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest23388():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200
