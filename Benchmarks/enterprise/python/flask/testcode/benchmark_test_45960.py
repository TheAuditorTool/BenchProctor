# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html


def BenchmarkTest45960(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
