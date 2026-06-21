# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest09672():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
