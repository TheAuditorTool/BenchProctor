# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest17729():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
