# SPDX-License-Identifier: Apache-2.0


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest53946(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
