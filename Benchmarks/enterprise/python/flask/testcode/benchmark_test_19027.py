# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest19027():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
