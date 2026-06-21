# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import time
from types import SimpleNamespace


def BenchmarkTest74403():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
