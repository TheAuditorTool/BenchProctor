# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify
import os
from types import SimpleNamespace


def BenchmarkTest43394():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ns = SimpleNamespace(payload=dotenv_value)
    data = getattr(ns, 'payload')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
