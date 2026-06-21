# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import pickle


def BenchmarkTest12417():
    env_value = os.environ.get('USER_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
