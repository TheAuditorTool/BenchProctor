# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest17862():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
