# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest77039(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    if session.get('role') != 'admin':
        return jsonify({'error': 'forbidden'}), 403
    session['data'] = str(data)
    return jsonify({"result": "success"})
