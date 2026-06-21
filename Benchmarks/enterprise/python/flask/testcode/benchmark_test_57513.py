# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest57513(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
