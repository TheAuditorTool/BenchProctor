# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify
from types import SimpleNamespace


def BenchmarkTest74789():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
