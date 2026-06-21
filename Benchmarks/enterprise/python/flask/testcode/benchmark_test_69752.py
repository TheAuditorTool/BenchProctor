# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest69752():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
