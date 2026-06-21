# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib


def BenchmarkTest07556():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
