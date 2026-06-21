# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest65215():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
