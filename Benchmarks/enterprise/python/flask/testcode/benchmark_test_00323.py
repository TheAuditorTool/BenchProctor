# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html


def BenchmarkTest00323(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
