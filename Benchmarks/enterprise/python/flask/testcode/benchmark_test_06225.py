# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest06225():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
