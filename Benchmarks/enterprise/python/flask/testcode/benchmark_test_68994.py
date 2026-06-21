# SPDX-License-Identifier: Apache-2.0
from flask import request


def normalise_input(value):
    return value.strip()

def BenchmarkTest68994():
    auth_header = request.headers.get('Authorization', '')
    data = normalise_input(auth_header)
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
