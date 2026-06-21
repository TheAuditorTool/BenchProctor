# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest29090():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
