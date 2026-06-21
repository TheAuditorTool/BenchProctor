# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request
from types import SimpleNamespace


def BenchmarkTest74860():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    def _primary():
        return redirect(str(data))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
