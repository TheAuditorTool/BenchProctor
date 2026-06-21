# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
from types import SimpleNamespace


def BenchmarkTest41376():
    origin_value = request.headers.get('Origin', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    return render_template_string(processed)
