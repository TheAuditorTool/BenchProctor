# SPDX-License-Identifier: Apache-2.0
import requests
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest74942():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
