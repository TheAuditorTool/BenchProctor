# SPDX-License-Identifier: Apache-2.0
from flask import request


def normalise_input(value):
    return value.strip()

def BenchmarkTest54606():
    host_value = request.headers.get('Host', '')
    data = normalise_input(host_value)
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
