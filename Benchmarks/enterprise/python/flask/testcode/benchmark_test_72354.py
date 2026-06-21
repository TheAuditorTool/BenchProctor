# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest72354():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
