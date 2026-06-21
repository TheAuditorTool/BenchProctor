# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html


def BenchmarkTest77810(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
