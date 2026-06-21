# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest32163():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
