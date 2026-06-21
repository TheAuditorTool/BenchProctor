# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest02732():
    auth_header = request.headers.get('Authorization', '')
    link_path = os.path.join('/var/app/data', str(auth_header))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
