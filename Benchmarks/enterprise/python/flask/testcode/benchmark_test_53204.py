# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse
from types import SimpleNamespace


def BenchmarkTest53204():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
