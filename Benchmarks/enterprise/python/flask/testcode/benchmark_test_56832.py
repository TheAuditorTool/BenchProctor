# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest56832():
    xml_value = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    return str(data), 200, {'Content-Type': 'text/html'}
