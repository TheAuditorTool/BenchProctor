# SPDX-License-Identifier: Apache-2.0
import json
from flask import request


def BenchmarkTest30918():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
