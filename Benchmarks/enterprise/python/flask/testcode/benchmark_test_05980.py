# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
import defusedxml.ElementTree


def BenchmarkTest05980():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
