# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest07376():
    host_value = request.headers.get('Host', '')
    data = to_text(host_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
