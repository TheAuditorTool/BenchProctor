# SPDX-License-Identifier: Apache-2.0
import json
from flask import request
import os


def BenchmarkTest27082():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
