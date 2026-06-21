# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest56067():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
