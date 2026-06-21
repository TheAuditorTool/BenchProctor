# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest49766():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = RequestPayload(config_value).value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
