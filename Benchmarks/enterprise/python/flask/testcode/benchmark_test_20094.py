# SPDX-License-Identifier: Apache-2.0
from flask import request
from types import SimpleNamespace


def BenchmarkTest20094():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
