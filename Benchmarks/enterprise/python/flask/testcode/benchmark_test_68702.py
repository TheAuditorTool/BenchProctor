# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def BenchmarkTest68702(path_param):
    path_value = path_param
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
