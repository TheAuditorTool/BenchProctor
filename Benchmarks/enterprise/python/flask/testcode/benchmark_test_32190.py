# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest32190():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    processed = data[:64]
    globals()['counter'] = int(processed)
    return jsonify({"result": "success"})
