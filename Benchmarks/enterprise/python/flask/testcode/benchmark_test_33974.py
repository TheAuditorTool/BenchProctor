# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import markdown
import bleach


def BenchmarkTest33974(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    processed = bleach.clean(markdown.markdown(data))
    return Markup('<div>' + str(processed) + '</div>')
