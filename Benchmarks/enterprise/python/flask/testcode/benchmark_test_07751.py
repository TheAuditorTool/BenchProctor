# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest07751():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
