# SPDX-License-Identifier: Apache-2.0
import requests
import os


def BenchmarkTest22596():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
