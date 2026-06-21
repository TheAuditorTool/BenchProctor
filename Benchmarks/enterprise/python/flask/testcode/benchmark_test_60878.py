# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest60878():
    upload_name = request.files['upload'].filename
    data = RequestPayload(upload_name).value
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
