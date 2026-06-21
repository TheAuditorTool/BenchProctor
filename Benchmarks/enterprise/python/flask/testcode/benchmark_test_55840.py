# SPDX-License-Identifier: Apache-2.0
import os
import json
from flask import request


def BenchmarkTest55840():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
