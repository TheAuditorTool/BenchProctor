# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach


def BenchmarkTest12512(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
