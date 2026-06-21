# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html


def BenchmarkTest18865(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
