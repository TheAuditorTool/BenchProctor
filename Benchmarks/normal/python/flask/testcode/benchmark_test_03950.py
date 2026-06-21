# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest03950():
    xml_value = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
