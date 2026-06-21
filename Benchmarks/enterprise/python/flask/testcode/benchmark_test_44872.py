# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest44872():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
