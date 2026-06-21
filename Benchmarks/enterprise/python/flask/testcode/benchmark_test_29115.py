# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def BenchmarkTest29115():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
