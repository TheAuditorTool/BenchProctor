# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach


request_state: dict[str, str] = {}

def BenchmarkTest08827(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
