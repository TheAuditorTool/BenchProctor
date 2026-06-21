# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest11903():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
