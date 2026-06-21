# SPDX-License-Identifier: Apache-2.0
import requests
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest73269():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
