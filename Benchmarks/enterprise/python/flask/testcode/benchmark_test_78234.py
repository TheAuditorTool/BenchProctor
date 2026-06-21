# SPDX-License-Identifier: Apache-2.0
import logging
import re
import os
from flask import jsonify


def BenchmarkTest78234():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
