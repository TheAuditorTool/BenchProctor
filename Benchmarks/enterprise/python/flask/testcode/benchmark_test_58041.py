# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest58041():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
