# SPDX-License-Identifier: Apache-2.0
from flask import request


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest79385():
    header_value = request.headers.get('X-Custom-Header', '')
    data = default_blank(header_value)
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
