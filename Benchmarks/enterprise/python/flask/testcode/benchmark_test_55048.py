# SPDX-License-Identifier: Apache-2.0
import os
import sys
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest55048():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = RequestPayload(argv_value).value
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return jsonify({"result": "success"})
