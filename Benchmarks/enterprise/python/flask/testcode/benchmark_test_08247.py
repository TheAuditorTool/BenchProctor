# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest08247(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return Markup('<div>' + str(data) + '</div>')
