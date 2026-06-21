# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest71942():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = to_text(forwarded_ip)
    def _primary():
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
