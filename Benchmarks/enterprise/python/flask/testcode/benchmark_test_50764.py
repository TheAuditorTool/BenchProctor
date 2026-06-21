# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import re
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest50764(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return Markup('<div>' + str(processed) + '</div>')
