# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest50265():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
