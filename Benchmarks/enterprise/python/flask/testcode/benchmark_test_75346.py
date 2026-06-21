# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
import os
import ast


def BenchmarkTest75346():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
