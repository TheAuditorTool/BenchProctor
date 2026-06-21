# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
import defusedxml.ElementTree


def BenchmarkTest71404():
    ua_value = request.headers.get('User-Agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
