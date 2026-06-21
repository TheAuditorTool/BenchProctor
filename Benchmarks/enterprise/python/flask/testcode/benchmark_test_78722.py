# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest78722(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
