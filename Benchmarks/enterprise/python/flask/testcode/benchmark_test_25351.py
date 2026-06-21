# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from urllib.parse import unquote


def BenchmarkTest25351(path_param):
    path_value = path_param
    data = unquote(path_value)
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')
