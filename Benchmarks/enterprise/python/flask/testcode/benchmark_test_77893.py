# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html


request_state: dict[str, str] = {}

def BenchmarkTest77893(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    processed = str(data).replace("<script", "")
    return Markup('<div>' + str(processed) + '</div>')
