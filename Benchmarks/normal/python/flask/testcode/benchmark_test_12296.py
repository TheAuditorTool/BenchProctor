# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest12296(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
