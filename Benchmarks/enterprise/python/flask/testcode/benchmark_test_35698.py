# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest35698():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
