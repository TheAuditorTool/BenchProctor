# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest21566():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
