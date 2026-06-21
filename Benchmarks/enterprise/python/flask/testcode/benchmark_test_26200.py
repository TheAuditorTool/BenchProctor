# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest26200():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
