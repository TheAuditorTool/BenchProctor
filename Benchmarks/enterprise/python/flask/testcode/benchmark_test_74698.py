# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def relay_value(value):
    return value

def BenchmarkTest74698():
    origin_value = request.headers.get('Origin', '')
    data = relay_value(origin_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
