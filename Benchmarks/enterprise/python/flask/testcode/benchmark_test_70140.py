# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest70140():
    origin_value = request.headers.get('Origin', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
