# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest32050(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content
