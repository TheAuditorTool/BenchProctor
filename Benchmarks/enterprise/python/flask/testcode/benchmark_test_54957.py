# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest54957():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = RequestPayload(prop_value).value
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
