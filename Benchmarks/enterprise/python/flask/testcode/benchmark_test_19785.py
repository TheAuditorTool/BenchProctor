# SPDX-License-Identifier: Apache-2.0
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest19785():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    return str(data), 200, {'Content-Type': 'text/html'}
