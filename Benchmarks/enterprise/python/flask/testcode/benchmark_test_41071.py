# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest41071():
    field_value = request.form.get('field', '')
    data = coalesce_blank(field_value)
    def _primary():
        return redirect(str(data))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
