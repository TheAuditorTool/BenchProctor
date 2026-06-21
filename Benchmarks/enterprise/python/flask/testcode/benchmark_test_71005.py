# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest71005():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(forwarded_ip))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
