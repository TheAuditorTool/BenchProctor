# SPDX-License-Identifier: Apache-2.0
import requests


def BenchmarkTest37170(path_param):
    path_value = path_param
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
