# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest21492():
    xml_value = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    return str(data), 200, {'Content-Type': 'text/html'}
