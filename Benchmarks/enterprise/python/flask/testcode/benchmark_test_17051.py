# SPDX-License-Identifier: Apache-2.0
import yaml
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest17051():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
