# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest03307():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return jsonify({"result": "success"})
