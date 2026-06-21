# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest65984():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
