# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest10141():
    xml_value = request.get_data(as_text=True)
    data = RequestPayload(xml_value).value
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return jsonify({'config_set': 'APP_USER_PREFERENCE'}), 200
