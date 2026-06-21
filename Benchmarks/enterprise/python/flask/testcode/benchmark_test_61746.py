# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest61746():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
