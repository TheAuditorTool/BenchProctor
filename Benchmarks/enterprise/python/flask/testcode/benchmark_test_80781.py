# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest80781():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
