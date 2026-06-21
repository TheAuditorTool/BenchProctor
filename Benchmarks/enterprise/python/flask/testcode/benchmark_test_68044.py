# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest68044():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
