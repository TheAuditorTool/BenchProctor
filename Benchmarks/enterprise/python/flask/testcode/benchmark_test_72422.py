# SPDX-License-Identifier: Apache-2.0
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest72422():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
