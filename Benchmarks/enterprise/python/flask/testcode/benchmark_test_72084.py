# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup


def BenchmarkTest72084(path_param):
    path_value = path_param
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return Markup('<div>' + str(data) + '</div>')
