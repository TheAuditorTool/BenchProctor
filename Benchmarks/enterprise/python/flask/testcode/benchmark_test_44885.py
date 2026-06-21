# SPDX-License-Identifier: Apache-2.0


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest44885(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
