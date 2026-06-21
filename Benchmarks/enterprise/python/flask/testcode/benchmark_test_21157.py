# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import re


def BenchmarkTest21157():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
