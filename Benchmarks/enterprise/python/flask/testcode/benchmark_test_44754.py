# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest44754():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
