# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest06675(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return str(data), 200, {'Content-Type': 'text/html'}
