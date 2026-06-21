# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest10884():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    return str(data), 200, {'Content-Type': 'text/html'}
