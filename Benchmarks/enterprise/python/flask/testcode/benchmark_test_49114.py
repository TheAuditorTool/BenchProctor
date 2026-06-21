# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html


def BenchmarkTest49114(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
