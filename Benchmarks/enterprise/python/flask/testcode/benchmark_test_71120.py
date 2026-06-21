# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest71120():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    globals()['counter'] = int(processed)
    return jsonify({"result": "success"})
