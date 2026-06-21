# SPDX-License-Identifier: Apache-2.0
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest21146():
    xml_value = request.get_data(as_text=True)
    data = to_text(xml_value)
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
