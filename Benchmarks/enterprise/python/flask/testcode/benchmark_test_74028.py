# SPDX-License-Identifier: Apache-2.0
import requests
import os


def BenchmarkTest74028():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
