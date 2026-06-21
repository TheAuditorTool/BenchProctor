# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json


def BenchmarkTest63207():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    json.loads(data)
    return jsonify({"result": "success"})
