# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest15566():
    host_value = request.headers.get('Host', '')
    link_path = os.path.join('/var/app/data', str(host_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
