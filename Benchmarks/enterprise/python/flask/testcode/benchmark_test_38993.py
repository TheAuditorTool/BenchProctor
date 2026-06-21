# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest38993():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
