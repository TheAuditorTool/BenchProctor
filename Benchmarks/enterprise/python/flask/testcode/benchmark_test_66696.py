# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest66696():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
