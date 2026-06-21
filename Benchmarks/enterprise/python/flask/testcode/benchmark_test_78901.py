# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest78901():
    xml_value = request.get_data(as_text=True)
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    return str(data), 200, {'Content-Type': 'text/html'}
