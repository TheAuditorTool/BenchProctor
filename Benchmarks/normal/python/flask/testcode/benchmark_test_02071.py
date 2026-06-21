# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest02071():
    xml_value = request.get_data(as_text=True)
    return '<html><body><h1>' + str(xml_value) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
