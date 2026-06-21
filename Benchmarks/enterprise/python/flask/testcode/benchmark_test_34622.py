# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest34622():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
