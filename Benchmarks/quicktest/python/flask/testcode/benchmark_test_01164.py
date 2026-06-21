# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
from types import SimpleNamespace


def BenchmarkTest01164():
    host_value = request.headers.get('Host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return render_template_string(processed)
