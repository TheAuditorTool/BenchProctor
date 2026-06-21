# SPDX-License-Identifier: Apache-2.0
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest68229():
    auth_header = request.headers.get('Authorization', '')
    data = ensure_str(auth_header)
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
