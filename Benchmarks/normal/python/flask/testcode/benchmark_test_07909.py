# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def BenchmarkTest07909():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
