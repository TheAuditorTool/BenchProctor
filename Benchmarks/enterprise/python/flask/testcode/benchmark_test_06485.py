# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest06485():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
