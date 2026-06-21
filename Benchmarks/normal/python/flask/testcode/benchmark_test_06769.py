# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest06769():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    return str(data), 200, {'Content-Type': 'text/html'}
