# SPDX-License-Identifier: Apache-2.0
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest13034():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
