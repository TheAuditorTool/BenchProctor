# SPDX-License-Identifier: Apache-2.0
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest40591():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    return str(data), 200, {'Content-Type': 'text/html'}
