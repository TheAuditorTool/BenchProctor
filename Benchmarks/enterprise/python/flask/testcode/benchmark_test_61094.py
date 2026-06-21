# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest61094():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
