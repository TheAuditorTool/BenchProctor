# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest07578(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    return Markup('<div>' + str(data) + '</div>')
