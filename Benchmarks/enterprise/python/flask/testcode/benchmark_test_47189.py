# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest47189():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
