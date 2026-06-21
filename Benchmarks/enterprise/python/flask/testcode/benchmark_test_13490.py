# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest13490(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
