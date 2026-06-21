# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest48582(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
