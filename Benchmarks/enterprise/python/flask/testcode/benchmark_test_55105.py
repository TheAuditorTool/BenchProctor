# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request


def coalesce_blank(value):
    return value or ''

def BenchmarkTest55105():
    field_value = request.form.get('field', '')
    data = coalesce_blank(field_value)
    def _primary():
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
