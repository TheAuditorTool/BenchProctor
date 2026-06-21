# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string


def BenchmarkTest02968(path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    return render_template_string(data)
