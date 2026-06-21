# SPDX-License-Identifier: Apache-2.0
import os


def BenchmarkTest42005():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
