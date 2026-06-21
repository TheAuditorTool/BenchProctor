# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest67407():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
