# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest52711():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
