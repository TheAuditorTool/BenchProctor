# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest33853():
    origin_value = request.headers.get('Origin', '')
    data = coalesce_blank(origin_value)
    def _primary():
        return render_template_string(data)
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
