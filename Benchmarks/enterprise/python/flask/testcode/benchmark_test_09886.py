# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest09886():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = RequestPayload(prop_value).value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
