# SPDX-License-Identifier: Apache-2.0


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest70736(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
