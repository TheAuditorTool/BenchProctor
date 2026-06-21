# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest49347():
    xml_value = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(xml_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
