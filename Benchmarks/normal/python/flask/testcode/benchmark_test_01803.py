# SPDX-License-Identifier: Apache-2.0
import json
from flask import request


def BenchmarkTest01803():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
