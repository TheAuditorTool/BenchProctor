# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest27987():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
