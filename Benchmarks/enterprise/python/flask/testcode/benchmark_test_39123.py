# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest39123(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
