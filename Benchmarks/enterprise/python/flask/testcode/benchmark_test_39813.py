# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request
import os


def BenchmarkTest39813():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
