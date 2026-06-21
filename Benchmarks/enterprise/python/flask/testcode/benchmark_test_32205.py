# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import auth_check


def BenchmarkTest32205():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = '%s' % (dotenv_value,)
    auth_check('user', data)
    return jsonify({"result": "success"})
