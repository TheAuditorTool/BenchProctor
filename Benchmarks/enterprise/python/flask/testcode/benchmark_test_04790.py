# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html


def BenchmarkTest04790(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
