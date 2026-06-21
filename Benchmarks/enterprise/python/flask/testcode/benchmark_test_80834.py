# SPDX-License-Identifier: Apache-2.0
from flask import request
from types import SimpleNamespace


def BenchmarkTest80834():
    referer_value = request.headers.get('Referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
