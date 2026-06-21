# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest04243():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
