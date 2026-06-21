# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest05196():
    upload_name = request.files['upload'].filename
    data = RequestPayload(upload_name).value
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
