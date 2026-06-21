# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest09634():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
