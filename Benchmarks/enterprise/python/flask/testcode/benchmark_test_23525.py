# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest23525():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
