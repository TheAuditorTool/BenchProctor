# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest09980():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    return str(data), 200, {'Content-Type': 'text/html'}
