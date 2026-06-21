# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def ensure_str(value):
    return str(value)

def BenchmarkTest47949():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
