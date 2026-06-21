# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest47654():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
