# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest28215():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
