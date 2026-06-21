# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest04800():
    xml_value = request.get_data(as_text=True)
    with open('/var/app/data/' + str(xml_value), 'r') as fh:
        content = fh.read()
    return content
