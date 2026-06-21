# SPDX-License-Identifier: Apache-2.0
import json
from flask import request


def BenchmarkTest27444():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
