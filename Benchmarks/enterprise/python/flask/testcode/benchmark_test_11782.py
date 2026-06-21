# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import bleach


def BenchmarkTest11782(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    processed = bleach.clean(data)
    return Markup('<div>' + str(processed) + '</div>')
