# SPDX-License-Identifier: Apache-2.0
import logging
import os
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest03297():
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
