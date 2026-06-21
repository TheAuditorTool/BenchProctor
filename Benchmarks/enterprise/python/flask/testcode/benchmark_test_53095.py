# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest53095():
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
