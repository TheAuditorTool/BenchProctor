# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest01543():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
