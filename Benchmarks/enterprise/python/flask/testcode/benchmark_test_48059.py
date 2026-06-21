# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest48059():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
