# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html


def BenchmarkTest08512(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')
