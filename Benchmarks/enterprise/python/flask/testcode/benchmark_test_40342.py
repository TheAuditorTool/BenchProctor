# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest40342():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
