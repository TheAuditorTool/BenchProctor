# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest14639():
    header_value = request.headers.get('X-Custom-Header', '')
    data = default_blank(header_value)
    def _primary():
        return redirect(str(data))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
