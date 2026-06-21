# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest04732():
    xml_value = request.get_data(as_text=True)
    data, _sep, _rest = str(xml_value).partition('\x00')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
