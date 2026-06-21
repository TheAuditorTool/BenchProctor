# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest38729():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
