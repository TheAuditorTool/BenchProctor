# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest58354(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
