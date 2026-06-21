# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest78525():
    origin_value = request.headers.get('Origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
