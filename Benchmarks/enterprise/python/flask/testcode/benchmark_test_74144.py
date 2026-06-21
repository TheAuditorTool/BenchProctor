# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest74144():
    multipart_value = request.form.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    os.remove(str(data))
    return jsonify({"result": "success"})
