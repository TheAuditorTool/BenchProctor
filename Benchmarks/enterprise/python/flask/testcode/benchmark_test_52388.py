# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest52388():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
