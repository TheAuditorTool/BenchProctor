# SPDX-License-Identifier: Apache-2.0
import os
import requests
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest26417():
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = RequestPayload(api_value).value
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
