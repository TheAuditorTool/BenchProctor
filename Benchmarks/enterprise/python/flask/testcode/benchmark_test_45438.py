# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest45438():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
