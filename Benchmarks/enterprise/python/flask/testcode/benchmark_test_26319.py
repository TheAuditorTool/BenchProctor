# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest26319():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
