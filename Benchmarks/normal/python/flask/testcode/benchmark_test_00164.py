# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request
from types import SimpleNamespace


def BenchmarkTest00164():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    return redirect(str(processed))
