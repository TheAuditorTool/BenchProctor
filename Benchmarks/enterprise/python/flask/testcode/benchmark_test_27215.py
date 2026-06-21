# SPDX-License-Identifier: Apache-2.0


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest27215(path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
