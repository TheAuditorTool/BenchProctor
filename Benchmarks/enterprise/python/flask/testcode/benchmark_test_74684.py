# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import tempfile


def BenchmarkTest74684():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
