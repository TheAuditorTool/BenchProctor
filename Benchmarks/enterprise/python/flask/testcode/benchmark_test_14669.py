# SPDX-License-Identifier: Apache-2.0
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14669():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
