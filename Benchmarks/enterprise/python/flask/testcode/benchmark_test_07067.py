# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def BenchmarkTest07067():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
