# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest06222():
    auth_header = request.headers.get('Authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    def _primary():
        os.system('echo ' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
