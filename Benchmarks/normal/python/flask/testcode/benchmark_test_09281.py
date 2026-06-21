# SPDX-License-Identifier: Apache-2.0
import threading
import re
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest09281(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    globals()['counter'] = int(processed)
    return jsonify({"result": "success"})
