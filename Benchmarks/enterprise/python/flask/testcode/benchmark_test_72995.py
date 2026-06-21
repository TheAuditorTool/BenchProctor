# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach
import ast


def BenchmarkTest72995(path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
