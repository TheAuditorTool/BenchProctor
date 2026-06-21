# SPDX-License-Identifier: Apache-2.0
import requests
import os


def BenchmarkTest21667():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
