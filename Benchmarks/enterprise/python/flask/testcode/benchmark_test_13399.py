# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest13399():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
