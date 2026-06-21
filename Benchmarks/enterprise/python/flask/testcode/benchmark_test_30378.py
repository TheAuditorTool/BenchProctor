# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest30378():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
