# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest19386(path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    return Markup('<div>' + str(data) + '</div>')
