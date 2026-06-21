# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest42411():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    def _primary():
        return Markup('<div>' + str(data) + '</div>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
