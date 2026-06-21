# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest03704():
    upload_name = request.files['upload'].filename
    link_path = os.path.join('/var/app/data', str(upload_name))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
