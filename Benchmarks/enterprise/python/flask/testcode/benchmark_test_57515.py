# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest57515():
    field_value = request.form.get('field', '')
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
