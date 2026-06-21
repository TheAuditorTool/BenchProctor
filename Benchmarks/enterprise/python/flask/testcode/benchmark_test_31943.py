# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest31943(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return Markup('<img src="' + str(data) + '">')
