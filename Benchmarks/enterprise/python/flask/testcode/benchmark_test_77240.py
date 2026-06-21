# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest77240():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    return str(data), 200, {'Content-Type': 'text/html'}
