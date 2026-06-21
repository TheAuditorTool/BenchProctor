# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest58455():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
