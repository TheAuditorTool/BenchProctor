# SPDX-License-Identifier: Apache-2.0
import logging
import re
import os
from flask import jsonify


def BenchmarkTest06512():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
