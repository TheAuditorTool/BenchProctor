# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest44584():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
