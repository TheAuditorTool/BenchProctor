# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest66442():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
