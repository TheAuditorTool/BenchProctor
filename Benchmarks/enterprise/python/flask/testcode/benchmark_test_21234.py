# SPDX-License-Identifier: Apache-2.0
import requests
import os


def BenchmarkTest21234():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
