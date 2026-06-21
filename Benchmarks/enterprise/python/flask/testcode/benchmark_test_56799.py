# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
from types import SimpleNamespace


def BenchmarkTest56799():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
