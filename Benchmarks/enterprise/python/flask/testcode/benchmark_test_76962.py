# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest76962():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    session['data'] = str(data)
    return jsonify({"result": "success"})
