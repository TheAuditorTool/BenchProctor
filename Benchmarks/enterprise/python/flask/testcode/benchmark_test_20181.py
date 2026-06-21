# SPDX-License-Identifier: Apache-2.0


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest20181(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return '<!-- diagnostic build token: ' + str(data) + ' -->', 200, {'Content-Type': 'text/html'}
