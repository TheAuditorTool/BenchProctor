# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest38585():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
