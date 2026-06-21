# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest47133():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value}'
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
