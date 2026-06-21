# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest00247():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
