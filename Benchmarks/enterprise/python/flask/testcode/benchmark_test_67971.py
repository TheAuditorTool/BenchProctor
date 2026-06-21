# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse
from types import SimpleNamespace


def BenchmarkTest67971():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
