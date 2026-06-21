# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest76186(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
