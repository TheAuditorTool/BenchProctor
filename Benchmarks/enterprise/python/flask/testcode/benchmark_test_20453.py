# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import urllib.parse


def BenchmarkTest20453(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
