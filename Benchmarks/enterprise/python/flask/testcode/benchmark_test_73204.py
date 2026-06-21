# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
import defusedxml.ElementTree


def BenchmarkTest73204():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
