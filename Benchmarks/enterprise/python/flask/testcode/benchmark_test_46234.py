# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest46234():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
